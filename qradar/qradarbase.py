import json
import requests

class QRadarSetupError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr('%s' % self.msg)

class QRadarError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return repr('[%s]: %s' % (self.code, self.msg))

class QRadarAPI(object):
    def __init__(self, host, port=443, ssl_verify=False, scheme='https', timeout=10):
        self.session = requests.Session()
        self.scheme = scheme
        self.host = host
        self.port = port
        self.ssl_verify = ssl_verify
        self.timeout = timeout

    def _url_builder(self, path, id=""):
        url = "%s://%s:%s/api/%s" % (self.scheme, self.host, self.port, path)

		# Might be legacy
        if id:
            try:
                url += "/%s" % int(id)
            except ValueError:
                raise QRadarError("405", "\"Id\" needs to be an integer.")

        return url

    def _kwarg_builder(self, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = self.header

        kwargs['verify'] = self.ssl_verify
        kwargs['timeout'] = self.timeout

        # Add json data recognition for json= or data=

        if not self.ssl_verify:
            requests.packages.urllib3.disable_warnings(\
                requests.packages.urllib3.exceptions.InsecureRequestWarning)

        return kwargs

    def _resp_error_check(self, response):
        try:
            d = response.json()

            if response.status_code != 200:
                raise QRadarError(response.status_code, d["message"])
        except ValueError:
            pass

        return response

    def get(self, path, **kwargs):
        response = self.session.get(self._url_builder(path),\
            **self._kwarg_builder(**kwargs))

        return self._resp_error_check(response)

    # Check for data.
    def post(self, path, **kwargs):
        response = self.session.post(self._url_builder(path),\
            **self._kwarg_builder(**kwargs))

        return self._resp_error_check(response)

    def put(self, path, **kwargs):
        response = self.session.put(self._url_builder(path),\
            **self._kwarg_builder(**kwargs))

        return self._resp_error_check(response)

    def delete(self, path, **kwargs):
        response = self.session.delete(self._url_builder(path),\
            **self._kwarg_builder(**kwargs))

        return self._resp_error_check(response)

    def head(self, path, **kwargs):
        response = self.session.head(self._url_builder(path),\
            **self._kwarg_builder(**kwargs))

        return self._resp_error_check(response)

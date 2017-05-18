import json
import requests

class QRadarError(Exception):
	def __init__(self, code, msg):
		self.code = code
		self.msg = msg

	def __str__(self):
		return repr('[%s]: %s' % (self.code, self.msg))

class QRadarAPI(object):
	def __init__(self, host, port=443, ssl_verify=False, scheme='https'):
		self.session = requests.Session()
		self.scheme = scheme
		self.host = host
		self.port = port
		self.ssl_verify = ssl_verify

	def _url_builder(self, pre, path, id=""):
		url = "%s://%s:%s/api/%s/%s" % (self.scheme, self.host, self.port, pre, path)
		if id:
			try:
				url += "/%s" % int(id)
			except ValueError:
				raise QRadarError("405", "Id needs to be an integer.")
			
		return url

	def _kwarg_builder(self, **kwargs):
		if "headers" not in kwargs:
			kwargs["headers"] = {}

		# Default set to false.
		kwargs['verify'] = self.ssl_verify

		if not self.ssl_verify:
			requests.packages.urllib3.disable_warnings(\
			requests.packages.urllib3.exceptions.InsecureRequestWarning)

		return kwargs

	def resp_error_check(self, response):
		try:
			d = response.json()

			if response.status_code != 200:
				raise QRadarError(response.status_code, d["message"])
		except ValueError:
			pass

		return response

	def verify_function(self, path, function, id=0):
		for item in json.load(open("database.json", "r")): 
			if item["name"] == path:
				if function not in item["function"]:
					raise QRadarError("405", "Function %s is not available for %s" % (function, item["parent"]))

				return item["parent"]

		return False

	def get(self, path, id=0, **kwargs):
		# Add error codes
		verification = self.verify_function(path, "GET", id)
		if not verification:
			raise QRadarError(405, "Error not implemented yet - either bad functionname or bad parameter for name.")
			
		resp = self.session.get(self._url_builder(verification, path, id), **self._kwarg_builder(**kwargs))
		if 'stream' in kwargs:
			return resp
		else:
			return self.resp_error_check(resp)

	def post(self, path, **kwargs):
		verification = self.verify_function(path, "POST", id)
		if not verification:
			raise QRadarError(405, "Error not implemented yet - either bad functionname or bad parameter for name.")

		# Might not work completly yet
		resp = self.session.post(self._url_builder(verification, path, id), **self._kwarg_builder(**kwargs))
		if 'stream' in kwargs:
			return resp
		else:
			return self.resp_error_check(resp).json()

	"""
	# Not yet fully implemented
	def delete(self, pre, path, **kwargs):
		resp = self.session.delete(self._url_builder(pre, path, id), **self._kwarg_builder(**kwargs))
		if 'stream' in kwargs:
			return resp
		else:
			return self.resp_error_check(resp)

	def put(self, pre, path, **kwargs):
		resp = self.session.delete(self._url_builder(pre, path, id), **self._kwarg_builder(**kwargs))
		if 'stream' in kwargs:
			return resp
		else:
			return self.resp_error_check(resp)
	"""

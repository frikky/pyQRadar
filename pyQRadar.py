from qradarbase import QRadarAPI, QRadarError, QRadarSetupError

# Replace object with \BaseAPI
class QRadar(QRadarAPI):
    def __init__(self, host, SEC_token='', port=443, ssl_verify=False, scheme='https'):
        if not SEC_token:
            raise QRadarSetupError("Usage: pyQRadar.QRadar(\"ip\",\"token\")") 

        self.header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Version': '7.0',
            'SEC': '%s' % SEC_token
        }

        QRadarAPI.__init__(self, host, port, ssl_verify, scheme)

    def login(self):
        # Attempting to remove the first part of this based on the API used
        # Might be a bad idea as you need admin for this one.
        return self.get('servers', headers=self.header)

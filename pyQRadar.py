from qradarbase import QRadarAPI, QRadarError 

# Replace object with \BaseAPI
class QRadar(QRadarAPI):
	def __init__(self, host, port=443, ssl_verify=False, scheme='https'):
		self.header = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Version': '7.0'
		}
			
		QRadarAPI.__init__(self, host, port, ssl_verify, scheme)

	def login(self, token):
		self.header["SEC"] = token

		# Attempting to remove the first part of this based on the API used
		response = self.post('servers', headers=self.header)
		print response
		if response.status_code == 200:
			print "Logged in."
		else:
			print "Some error :O"


if __name__ == "__main__":
	# IP in this one
	qradar = QRadar("<qradar IP>")

	# Token in this one. Nedds to be admin for some methods. 	
	asd = qradar.login("<token here>")

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
		response = self.get('data_classification', 'dsm_event_mappings', 50, headers=self.header)
		if response.status_code == 200:
			for items in asd.json():
				print items
			print "Logged in."
		else:
			print "Some error :O"


if __name__ == "__main__":
	# IP in this one
	qradar = QRadar()

	# Token in this one. Nedds to be admin for some methods. 	
	asd = qradar.login("")

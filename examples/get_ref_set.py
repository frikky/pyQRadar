import requests

# Example without API
def run_example():

	headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'Version': '7.0',
		'SEC': ''
	}

	ip = ""
	req = requests.get("https://%s/api/reference_data/sets" % ip, headers=headers, verify=False)
	print req.json()

if __name__ == "__main__":
	run_example()

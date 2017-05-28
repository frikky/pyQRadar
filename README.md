# QRadar API wrapper

This is an attempt at creating a complete library for the QRadar API with error checks before the user makes mistakes. The main issue with the normal API is the folder structure used. 

[QRadar API](https://www.ibm.com/support/knowledgecenter/en/SSKMKU/com.ibm.qradar.doc/c_rest_api_whats_new_726.html)

[QRadar example repository without the library](https://github.com/ibm-security-intelligence/api-samples) 

# Installation 

Installation is made public in pypi and easy\_install.

`pip install pyqradar`

`easy_instal install pyqradar`

# Usage
The project is a simple wrapper to remove the need for handling via Requests. Below is a test to see if you have admin rights where it checks for system/servers.  

	>>> import qradar 
	>>> qradar = qradar.QRadar('HOSTNAME', 'SECtoken')
	>>> qradar.login()
	'Admin priviliges available.'

Further documentation will be made available as it gets tested more.

# Todo
* (DONE) - Make it available in easy\_install/pip
* (DONE) - Make import easier without "from qradar import pyQRadar" (init file)
* (DONE) - Set default headers, to make it uneccessary in get/post etc.
* (Started) - Create examples for how to use it.
* Create multiple error checks, especially for destructive constructs like DELETE and PUT. 
* Return json objects instead of plain data.
* Further testing of all request types.
* Have further header information checks.
* Add logging
* (DONE) - Add timeouts - Default set to 10
* Make it work for python 3 - It might actually work already if built from source.
* Add a changelog for versions

# QRadar API wrapper

This is an attempt at creating a complete library for the QRadar API with error checks before the user makes mistakes. The main issue with the normal API is the folder structure used. 

[QRadar API](https://www.ibm.com/support/knowledgecenter/en/SSKMKU/com.ibm.qradar.doc/c_rest_api_whats_new_726.html)

[QRadar example repository without the library](https://github.com/ibm-security-intelligence/api-samples) 

# Installation 

Installation is made public in pypi and easy\_install.

`pip install pyqradar`

`easy_instal install pyqradar`

# Usage
The project is not yet production level. Do not use it yet, but it works for simple tests.

The project is a simple wrapper to remove the need for handling via Requests. Available functions are login(), get(), post(), delete() and put(). login() is not required, but is a test to see if you have admin rights where it checks for system/servers. Below is a simple code test:

	>>> import qradar 
	>>> qradar = qradar.QRadar('HOSTNAME')
	>>> qradar.login()

# Todo
* (DONE) - Make it available in easy\_install/pip
* Create error checks, especially for DELETE and PUT functions. 
* Create examples for how to use it.
* Further testing of all request types.
* Have further header information checks.
* Add logging
* Make it work for python 3

# Why it sucks currently
This was done in about four hours, so don't expect it to work properly yet.

# Local Environment File Readme
This folder exists for users to add any and all python files that contain private data in them to them.

The minimum required files that the user must create are:
1. localapikeys.py
	* Must define the following variables in this file:
		* ```google_cse_api_key='api_key_string'```
		* ```google_cse_eng_id='engine_id_string'```
	* To acquire a google API key to use the custom search engine, a google API account must be made:
		* Acquiring API Key: https://developers.google.com/custom-search/v1/overview
		* Google CSE API Tutorial: https://www.youtube.com/watch?v=ScdA3q9y2Y8
2. localuser.py
   * Must contain declaration of variable django_production_key, which is a 50-digit secret key
   * In form ```django_production_key = 'secret_key_string'```
   * There are various ways to generate random keys--for instance, DJango automatically generates one when a new project is started.
   * This stackoverflow article explains how to generate secret keys: https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys
   * This website has an automatic secret key generator: https://www.miniwebtool.com/django-secret-key-generator/
3. localwebproxy.py


## Local API Key File Example
**Note**: The APIKey numbers below are not valid--you will need to generate them yourself
```#!/usr/bin/env python

"""	API Key Local Definitions File
	The purpose of this local file is to store all of the user's sensitive
	API keys so that they don't accidentally place them into the guts of their
	code that gets uploaded to the public git repository. For privacy reasons,
	this file has been added to the repository and restricted from the
	work-tree search so that it doesn't get accidentally added when triggering
	a git commit -a, eventually being pushed up to the remote master. Usage
	notes are in the local API keys subsection.
"""


# =============================================================================
# [1] Document Metadata
# =============================================================================
__author__    = 'Lennard Streat'
__copyright__ = 'Network of Intel African Americans 2019, PyStockAnalyze Project'
__credits__   = ['Lennard Streat', 'Princton Brennan']
__license__   = 'MIT'
__version__   = '1.0'
__email__     = 'nia.stem.club'


# =============================================================================
# [2] Local API Keys
# -----------------------------------------------------------------------------
# - To use this file the user should define global variables here that are then
#	utilized in the code; Some example variables have been added for reference
# =============================================================================
# Google Custom Search Engine
google_cse_api_key='012345678901234567890123456789012345678'
google_cse_eng_id='012345678901234567890:01234567890'
```

## Local User File Example
**Note**: The production secret key displayed below is just to give an example of how long the key is, but isn't a particularly good secret key--though it works for debug purposes
```
#!/usr/bin/env python

"""	General User Local Definitions File
	The purpose of this local file is to store all of the user's sensitive
	variables so that they don't accidentally place them into the guts of their
	code that gets uploaded to the public git repository. For privacy reasons,
	this file has been added to the repository and restricted from the
	work-tree search so that it doesn't get accidentally added when triggering
	a git commit -a, eventually being pushed up to the remote master. Usage
	notes are in the local user parameters subsection.
"""


# =============================================================================
# [1] Document Metadata
# =============================================================================
__author__    = 'Lennard Streat'
__copyright__ = 'Network of Intel African Americans 2019, PyStockAnalyze Project'
__credits__   = ['Lennard Streat', 'Princton Brennan']
__license__   = 'MIT'
__version__   = '1.0'
__email__     = 'nia.stem.club'


# =============================================================================
# [2] Local User Parameters
# -----------------------------------------------------------------------------
# - To use this file the user should define global variables here that are then
#	utilized in the code; Some example variables have been added for reference
# =============================================================================
# Django production key should be kept private
# Generate one from here: https://djecrety.ir/
django_production_key='01234567890123456789012345678901234567890123456789'

# Database Passwords
sqlite_pass=''

# User Passwords
user_admin_pass=''
```

## Local Web Proxy File Example
**Note**: The proxy port and host used below point to the default localhost, if a proxy is required, these need to be changed; If no proxy is to be used, the proxy_enabled flag needs to be made false
```
#!/usr/bin/env python

"""	Web Proxy Definitions File
	The purpose of this local file is to store all of the user's proxy-related
	information, so that these don't get uploaded to the public repository.
"""


# =============================================================================
# [1] Document Metadata
# =============================================================================
__author__    = 'Lennard Streat'
__copyright__ = 'Network of Intel African Americans 2019, PyStockAnalyze Project'
__credits__   = ['Lennard Streat', 'Princton Brennan']
__license__   = 'MIT'
__version__   = '1.0'
__email__     = 'nia.stem.club'


# =============================================================================
# [2] Local Proxy Parameters
# -----------------------------------------------------------------------------
# - To use this file the user should define global variables here that are then
#	utilized in the code; Some example variables have been added for reference
# =============================================================================
# Disable when working in an environment without an proxy server
proxy_enabled     = True

# To supply calls to httplib2
global_proxy_host = '127.0.0.1'
global_proxy_port = 80

# To supply calls to response
global_proxy_dict = {'https' : ':'.join([global_proxy_host,str(global_proxy_port)])}
```
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

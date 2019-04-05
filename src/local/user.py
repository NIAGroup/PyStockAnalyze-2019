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
# Database Passwords
sqlite_pass=''

# User Passwords
user_admin_pass=''

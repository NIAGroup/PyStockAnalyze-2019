"""	Google API Demo Example File
	This file contains a simple class that demonstrates how to access the google
	custom search engine (CSE) API to return a JSON object to be consumed
	by a DJANGO view to be displayed on a web page.
"""

# =============================================================================
# 1 | Document Metadata
# =============================================================================
__author__    = 'Lennard Streat'
__copyright__ = 'Network of Intel African Americans 2019, PyStockAnalyze Project'
__credits__   = ['Lennard Streat', 'Princton Brennan']
__license__   = 'MIT'
__version__   = '1.0'
__email__     = 'nia.stem.club'

# =============================================================================
# 2 | Imports
# =============================================================================
# Google CSE API Import
from googleapiclient.discovery import build

# Required packages for working with HTTP requests
import httplib2, requests, json, pprint

# Local imports
from pysdjango.localenv import localuser
from pysdjango.localenv import localapikeys
from pysdjango.localenv import localwebproxy

# =============================================================================
# 3 | Custom Search Engine Simple Query Class
# -----------------------------------------------------------------------------
# Takes a search string argument and sends that to the custom search API to
# search that string on the defined engine ID.
# =============================================================================
class CSEQuery:
	# Takes a string and returns a JSON object of the queried data received
	# From the google CSE
	def cse_search(search_string):
		# Example of a string to query google with
		cse_query_str = search_string
		httpreq = None

		# Utilize proxy if enabled
		if localwebproxy.proxy_enabled == True:
			# Example of a proxy object
			proxy_info = httplib2.ProxyInfo(proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
				proxy_host=localwebproxy.global_proxy_host,
				proxy_port=localwebproxy.global_proxy_port)

			# Example of an http request object
			httpreq = httplib2.Http(proxy_info = proxy_info)
		else:
			httpreq = httplib2.Http()

		# Google API CSE object construction
		service = build(serviceName='customsearch',
			version='v1',
			developerKey=localapikeys.google_cse_api_key,
			http=httpreq)

		resp = service.cse().list(
			q=cse_query_str,
			cx=localapikeys.google_cse_eng_id,
			).execute()

		return resp

	# Calls the CSE and converts the JSON object to a prettified string
	def cse_format(search_string):
		resp = CSEQuery.cse_search(search_string)
		return pprint.pformat(resp)
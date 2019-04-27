from googleapiclient.discovery import build

from googleapi_basic.localenv import localapikeys
from googleapi_basic.localenv import localwebproxy
import httplib2, requests, json

import pprint

class CSEQuery:
	def cse_search(search_string):
		# Example of a string to query google with
		cse_query_str = search_string; #"INTC"

		# Example of a proxy object
		proxy_info = httplib2.ProxyInfo(proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
			proxy_host=localwebproxy.global_proxy_host,
			proxy_port=localwebproxy.global_proxy_port)

		# Example of an http request object
		httpreq = httplib2.Http(proxy_info = proxy_info)

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

	def cse_format(search_string):
		resp = CSEQuery.cse_search(search_string)
		return pprint.pformat(resp)
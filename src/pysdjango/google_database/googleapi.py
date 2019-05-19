# =============================================================================
# 2 | Imports
# =============================================================================
# Google CSE API Import
from googleapiclient.discovery import build

# Required packages for working with HTTP requests
import httplib2
import requests
import json
import pprint as pp
# Local imports
from pysdjango.localenv import localuser
from pysdjango.localenv import localapikeys
from pysdjango.localenv import localwebproxy
from google_database import parsedata

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
            httpreq = httplib2.Http(proxy_info=proxy_info)
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

    def cse_imagesDescriptons(resp):
        imageDesc = []
        for i in resp['items']:
            tmp = []
            try:
                tmp.append(i['pagemap']['cse_image'][0]['src'])
            except:
                tmp.append("/static/google_database/default-image.jpg")

            try:
                tmp.append(i['pagemap']['metatags'][0]['og:description'])
            except:
                tmp.append("No description")
            imageDesc.append(tmp)
        return imageDesc

    # Calls the CSE and converts the JSON object to a prettified string
    def cse_format(search_string):
        resp = CSEQuery.cse_search(search_string)
        imageDesc = CSEQuery.cse_imagesDescriptons(resp)
        # return pp.pformat(resp, indent=4)
        return imageDesc, resp

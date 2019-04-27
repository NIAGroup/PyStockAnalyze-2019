from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyCpjSn7wj01RFrd9kB4qPqLaYTiMF_1Ptk"
my_cse_id = "002012074957532801967:mw1fj9u7p4m"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('bitcoin', my_api_key, my_cse_id, num=10)

for result in results:
    #pprint.pprint(result)

    title = result['title'].replace("\n","")
    link = result['formattedUrl']
    dis = result['snippet']
    print (f'~~~{title}')
    print (link)
    print (dis)
import json
import requests

ACL_CONSUMERKEY = ''
url = 'https://api-tokyochallenge.odpt.org/'
api = 'api/v4/odpt:TrainTimetable?'
acl = 'acl:consumerKey=ACL_CONSUMERKEY'

q = 'dc:title=東京&'

url = url+api+acl

data = requests.get(url)




def j_dump(data):
  format_json = json.dumps(data, indent=4, separators=(',', ': '))
  print(ormat_json)

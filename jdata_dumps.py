import json
import requests

ACL_CONSUMERKEY = ''
url = 'https://api-tokyochallenge.odpt.org/api/v4/odpt:Train?acl:consumerKey=ACL_CONSUMERKEY'

data = requests.get(url)


def j_dump(data):
  format_json = json.dumps(data, indent=4, separators=(',', ': '))
  print(ormat_json)

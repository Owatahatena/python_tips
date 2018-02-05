from requests_oauthlib import OAuth1Session
import json

session = OAuth1Session(c_k,c_s,a_t,a_s)
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

response = session(url)
print(response.json())

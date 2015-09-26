# Credits
#   http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# Installation
# sudo pip install requests requests_toolbelt requests_oauthlib

import requests

print ("\n##########> Response Content")

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get("http://httpbin.org/get", params=payload)

print ("url: %s" % r.url)
print ("status_code: %s check: %s" % (r.status_code, r.status_code == requests.codes.ok))
print ("request headers: %s" % r.request.headers)
print ("response headers: %s" % r.headers)
print ("headers[content-type]: %s" % r.headers["content-type"])
print ("text: %s" % r.text)
print ("json(): %s" % r.json())

print ("\n##########> Binary data")
r = requests.get("http://httpbin.org/image/jpeg")
print ("image length: %s" % r.headers["content-length"])
print ("image type: %s" % r.headers["content-type"])

print ("\n##########> More complicated POST requests")
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

print ("\n##########> More complicated POST requests- json")
payload = {'some': 'data'}
r = requests.post("http://httpbin.org/post", json=payload)
print(r.text)

print ("\n##########> POST a Multipart-Encoded File")
files = {'file': open('./data/snake1.png', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
#print(r.text)
print(r.url)

print ("\n##########> POST a Multipart-Encoded File- send string as file")
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)

print ("\n##########> Response Status Codes- Bad status 404")
bad_r = requests.get('http://httpbin.org/status/404')
try:
    bad_r.raise_for_status()
except:
    print("Error: 404")

print ("\n##########> Cookies")
cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print (r.text)


print ("\n##########> Redirection and History")
r = requests.get('http://github.com')
print (r.url)
print (r.status_code)
print (r.history)

print ("\n##########> Timeouts")
try:
    requests.get('http://github.com', timeout=0.001)
except:
    print("Request time outed")


print ("\n##########> Session Objects- Login to github")
with requests.Session() as s:
    s.auth = ('user', 'pass') # replace user,pass with real one
    r = s.get("https://api.github.com/user/emails")
    print(r.text)
    r = s.get("https://api.github.com/user")
    print(r.text)

#print ("\n##########> Streaming Uploads")
#with open('./data/snake1.png', 'rb') as f:
#    requests.post('http://some.url/streamed', data=f)

print ("\n##########> POST Multiple Multipart-Encoded Files")
multiple_files = [('images', ('snake1.png', open('./data/snake1.png', 'rb'), 'image/png')),
                      ('images', ('snake2.png', open('./data/snake2.png', 'rb'), 'image/png'))]
r = requests.post("http://httpbin.org/post", files=multiple_files)
#print (r.text) 
print (r.url)

print ("\n##########> POST Multiple Multipart-Encoded Files - Advanced")
# http://toolbelt.readthedocs.org/en/latest/uploading-data.html
# install
# pip install requests_toolbelt
from requests_toolbelt.multipart.encoder import MultipartEncoder
m = MultipartEncoder(
    fields={'field0': 'value', 'field1': 'value',
            'field2': ('filename', open('./data/snake1.png', 'rb'), 'text/plain')}
    )

r = requests.post('http://httpbin.org/post', data=m,
                  headers={'Content-Type': m.content_type})
print(r.url)
                  
print ("\n##########> Event Hooks")
def print_url(r, *args, **kwargs):
    print(r.url)
    
requests.get('http://httpbin.org', hooks=dict(response=print_url))

print ("\n##########> Streaming Requests")
r = requests.get('http://httpbin.org/stream/20', stream=True)
lines = r.iter_lines()
# Save the first line for later or just skip it
first_line = next(lines)
for line in lines:
    print(line)

#print ("\n##########> Proxies")
#proxies = {
#  "http": "http://user:pass@10.10.1.10:3128/",
#  "https": "http://10.10.1.10:1080",
#}
#requests.get("http://example.org", proxies=proxies)

#print ("\n##########> Digest Authentication")
#from requests.auth import HTTPDigestAuth
#url = 'http://httpbin.org/digest-auth/auth/user/pass'
#requests.get(url, auth=HTTPDigestAuth('user', 'pass'))

#print ("\n##########> OAuth 1 Authentication")
# installation
# pip install requests requests_oauthlib
#from requests_oauthlib import OAuth1Session
#twitter = OAuth1Session('client_key',
#                            client_secret='client_secret',
#                            resource_owner_key='resource_owner_key',
#                            resource_owner_secret='resource_owner_secret')
#r = twitter.get('https://api.twitter.com/1/account/settings.json')

#print ("\n##########> OAuth 2 Authentication")
#from requests_oauthlib import OAuth2Session
#google = OAuth2Session(r'client_id', token=r'token')
#r = google.get('https://www.googleapis.com/oauth2/v1/userinfo')


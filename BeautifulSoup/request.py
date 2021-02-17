install Request module

pip install requests

import requests

r = requests.get('https://xkcd.com/353/')

print(r)

print(r.text)

#Download image

r = requests.get('https://xkcd.com/comics/python.png')
print(r.content)

with open('comic.png', 'wb') as f:
  f.write(r.content)
  
  print(r.status_code)
  
   print(r.ok) # Print True for any response <400
   
  print(r.headers)
  
  https://httpbin.org
  
  # How to pass query parameter
  
  payload = {'page' : 2, 'count' :25}
  
  r = requests.get('https://httpbin.org/get', params=payload)
  print(r.text)
  
  
  ####### Post
  
  payload = {'username' : 'madhu', 'password' :'testing'}
  r = requests.post('https://httpbin.org/post', data=payload)
 r_dict = r.json() 
 
 print(r_dict['form'])
 
 
 ## timeout
 
 r = requests.get('https://xkcd.com/comics/python.png', timeout=3)
# if the request don't respond within 3 sec, timeout

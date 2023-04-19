# -*- coding: utf-8 -*-
import urllib.request
import requests
import json

class user:
  def __init__(self, email, password):   
    self.email = email
    self.password = password

  def __str__(self):
    return f'\nEmail: {self.email}\nPassword: {self.password}'   

user1 = user('admin@admin.com', '12345')
usr1 = json.dumps(user1.__dict__)    

headers = {
    'Content-Type': 'application/json',
    'X-eBirdApiToken': 'NaN',
}

url = requests.post("http://137.184.45.229:3001/api/v1/auth/login", usr1, headers)

print(url, url.headers, "Api:",url.text,'\n', usr1)
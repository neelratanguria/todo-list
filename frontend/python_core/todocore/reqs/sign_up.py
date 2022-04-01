import requests
import os
from .keys import APP_ID, APP_KEY

def sign_up(email, password):
    #payload = {'username': email, 'password': password}
    payload = {"email" : email, "password": password}
    print(payload)
    headers = {'X-Parse-Application-Id': APP_ID,
               'X-Parse-REST-API-Key' : APP_KEY}
    r = requests.post('https://parseapi.back4app.com/parse/functions/v1_sign_up', params=payload, headers=headers)
    print(r.json())
    if r.status_code == 200:    
        response_data = r.json()
        return True, response_data['result']["objectId"]
    else:
        return False, ""

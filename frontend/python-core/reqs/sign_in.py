import requests
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

def sign_in_request(email, password):
    payload = {'username': email, 'password': password}
    headers = {'X-Parse-Application-Id': APP_ID,
               'X-Parse-REST-API-Key' : APP_KEY}
    r = requests.get('https://parseapi.back4app.com/login', params=payload, headers=headers)
    if r.status_code == 200:    
        response_data = r.json()
        return response_data["objectId"] 
    else:
        raise Exception("Invalid login")
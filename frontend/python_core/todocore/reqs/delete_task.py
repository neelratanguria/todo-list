import requests
import os
from .keys import APP_ID, APP_KEY

def delete_task (id):
    payload= {'task_id': id}
    headers = {'X-Parse-Application-Id': APP_ID,
               'X-Parse-REST-API-Key' : APP_KEY}
    
    r = requests.post('https://parseapi.back4app.com/parse/functions/v1_deletedTask', params=payload, headers=headers)
    if r.status_code == 200:    
        return True
    else:
        raise Exception("wrong user id")
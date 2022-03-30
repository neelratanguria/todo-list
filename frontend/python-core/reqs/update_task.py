import requests
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

def update_task (id, name):
    payload= {'user_id': id,'task_name':name}
    headers = {'X-Parse-Application-Id': APP_ID,
               'X-Parse-REST-API-Key' : APP_KEY}
    
    r = requests.post('https://parseapi.back4app.com/parse/functions/v1_createTask', params=payload, headers=headers)

    
    if r.status_code == 200:    
        response_data = r.json()
        #print(response_data["result"] )
        
        
        return response_data["result"]["message"]

     

    else:
        
        raise Exception("wrong user id")

q= update_task("djmIXK4Wj6","changed")
print(q)
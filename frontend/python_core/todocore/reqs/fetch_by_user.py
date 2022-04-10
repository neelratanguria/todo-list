import requests
import os
from .keys import APP_ID, APP_KEY

# APP_ID = os.environ["APP_ID"]
# APP_KEY = os.environ["APP_KEY"]


def read_task(id):
    payload = {'user_id': id}
    headers = {'X-Parse-Application-Id': APP_ID,
               'X-Parse-REST-API-Key': APP_KEY}
    r = requests.post('https://parseapi.back4app.com/parse/functions/v1_fetchByUser',
                      params=payload, headers=headers)
    if r.status_code == 200:
        response_data = r.json()
        all_user_tasks = []
        parse_tasks = response_data["result"]["tasks"]
        for i in range(0, len(parse_tasks)):
            all_user_tasks.append({
                "task": parse_tasks[i]["task"],
                "id": parse_tasks[i]['objectId']
            })
        return all_user_tasks
    else:
        raise Exception("wrong user id")


if __name__ == '__main__':
    print(read_task('djmIXK4Wj6'))

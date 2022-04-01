def append_parent_path():
    import sys
    import os
    # getting the name of the directory
    # where the this file is present.
    current = os.path.dirname(os.path.realpath(__file__))
    
    # Getting the parent directory name
    # where the current directory is present.
    parent = os.path.dirname(current)
    
    # adding the parent directory to 
    # the sys.path.
    sys.path.append(parent)

append_parent_path()

from todocore.reqs.create_task import create_task
from todocore.reqs.fetch_by_user import read_task
from todocore.reqs.sign_in import sign_in_request
from todocore.reqs.sign_up import sign_up
import os
import sys
testing = False

import json
user_authenticated = False
user_id = None

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
    user_authenticated = True
    user_id = data["objectId"]
except FileNotFoundError:
    pass


# if testing:
#     user_authenticated = True
#     user_id = "djmIXK4Wj6"

def select_task_options():
    print("Please select following options")
    print("1 - Create Task")
    print("2 - Fetch all")
    print("3 - Logout")
    print("4 - Exit")
    option = input("->")
    return option

def authenticate_user():
    print("Please enter your email id")
    email = input("->")
    print("Please enter your password")
    password = input("->")
    status, id = sign_in_request(email, password)
    global user_id
    global user_authenticated
    if status:
        user_id = id
        user_authenticated = True
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({"logged_in": True, "objectId" : user_id}, f, ensure_ascii=False, indent=4)
    else:
        print("Invalid logging")
        
def signup_user():
    print("Please enter your email id")
    email = input("->")
    print("Please enter your password")
    password = input("->")
    status, id = sign_up(email, password)
    global user_id
    global user_authenticated
    if status:
        user_id = id
        user_authenticated = True
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({"logged_in": True, "objectId" : user_id}, f, ensure_ascii=False, indent=4)
    else:
        print("Invalid sign up")
        
def display_user_tasks():
    tasks = read_task(user_id)
    if len(tasks) ==0 :
        print("")
        print("No tasks found! Please create task")
        print("")
        return
    for x in range(0, len(tasks)):
        ind = x + 1
        print(ind, " "+tasks[x])

def logout_user():
    os.remove('data.json')
    global user_id
    global user_authenticated
    user_id = ""
    user_authenticated = False

def exit_app():
    sys.exit()    
    

def runApp():
    print("running")
    while True:
        if user_authenticated:
            option = select_task_options()
            if option == '1':
                task = input("Please input a task: ")
                print(create_task(user_id, task))
            elif option == '2':
                display_user_tasks()
            elif option == '3':
                logout_user()
            elif option == '4':
                exit_app()
        else:
            print("Choose an option")
            print("1 - Sign in")
            print("2 - Sign up")
            print("3 - Exit")
            opt = input("->")
            if opt == '1':
                authenticate_user()
            elif opt == '2':
                signup_user()
            elif opt == '3':
                exit_app()
            else:
                print("Invalid command")
                


if __name__ == "__main__":
    runApp()


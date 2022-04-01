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
testing = False

user_authenticated = False
user_id = None
# if testing:
#     user_authenticated = True
#     user_id = "djmIXK4Wj6"

def select_task_options():
    print("Please select following options")
    print("1 - Create Task")
    print("2 - Fetch all")
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
    else:
        print("Invalid logging")
        
def display_user_tasks():
    tasks = read_task(user_id)
    for x in range(0, len(tasks)):
        ind = x + 1
        print(ind, " "+tasks[x])

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
        else:
            authenticate_user()


if __name__ == "__main__":
    runApp()

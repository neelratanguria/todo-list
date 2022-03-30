from python_core.reqs.create_task import create_task
print(create_task)

testing = True

user_authenticated = False
user_id = None
if testing:
    user_authenticated = True
    user_id = "djmIXK4Wj6"


def authenticate_user():
    if True:
        user_authenticated = True
        user_id = ""
    else:
        print("Invalid login")

def select_task_options():
    print("Please select following options")
    print("1 - Create Task")
    print("2 - Fetch all")
    option = input("->")
    return option

def runApp():
    print("running")
    while True:
        if user_authenticated:
            option = select_task_options()
            if option == '1':
                task = input("Please input a task: ")
                print(create_task(user_id, task))
        else:
            pass


if __name__ == "__main__":
    runApp()

from kivymd.app import MDApp
import sys
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from todocore.reqs.sign_up import sign_up
from todocore.reqs.sign_in import sign_in_request
from todocore.reqs.create_task import create_task
from todocore.reqs.fetch_by_user import read_task

screen_helper = """

ScreenManager:
    MenuScreen:
    ProfileScreen:
    Sign_in:
    After_login:
    Create_task:
    Read_task:
    Sign_up:
    ExitScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'exit'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'exit'
    
<ProfileScreen>:
    name: 'profile'
    MDRectangleFlatButton:
        text: 'Sign In'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'signin'
    MDRectangleFlatButton:
        text: 'Sign Up'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'signup'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<Sign_in>:
    name: 'signin'

    email: email
    password:password
    
    MDTextField:
        id : email
        size_hint: (0.8, None)
        hint_text: "Email id"
        mode: "rectangle"
        pos_hint: {'center_x':0.5,'center_y':0.6}

    MDTextFieldRound:
        id : password
        size_hint: (0.8, None)
        hint_text: "Password"
        mode: "rectangle"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        

    MDRectangleFlatButton:
        text: 'Sign in'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'afterlogin'

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'profile'

<After_login>:
    name: 'afterlogin'
    MDRectangleFlatButton:
        text: 'Create task'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'createtask'
    MDRectangleFlatButton:
        text: 'Read task'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'readtask'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'profile'

<Create_task>:
    name: 'createtask'

    note: note

    MDTextField:
        id: note
        multiline: True
        size_hint: (0.8, None)
        hint_text: "write a task"
        pos_hint: {'center_x':0.5,'center_y':0.6}

    MDRectangleFlatButton:
        text: 'Create task'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.task()
    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'afterlogin'

<Read_task>:
    name: 'readtask'

    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'afterlogin'

<Sign_up>:
    name: 'signup'
    email: email
    password:password
    
    MDTextField:
        id : email
        size_hint: (0.8, None)
        hint_text: "Email id"
        mode: "rectangle"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        
    
    MDTextFieldRound:
        id : password
        size_hint: (0.8, None)
        hint_text: "Password"
        mode: "rectangle"
        pos_hint: {'center_x':0.5,'center_y':0.5}


    MDRectangleFlatButton:
        text: 'Sign in'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'afterlogin'

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'profile'
        
<ExitScreen>:
    name: 'exit'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'menu'
    
    MDRectangleFlatButton:
        text: 'Exit'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.exit()
    
        
"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class Sign_in(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def btn(self):
        print("email:", self.email.text, "password:", self.password.text)
        self.email.text = ""
        self.password.text = ""

class After_login(Screen):
    pass

class Create_task(Screen):
    note = ObjectProperty(None)
    
    def task(self):
        print("task:", self.note.text)
        self.note.text = ""
        


class Read_task(Screen):
    print("working")


class Sign_up(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def btn(self):
        print("email:", self.email.text, "password:", self.password.text)
        self.email.text = ""
        self.password.text = ""

    

class ExitScreen(Screen):
    def exit(self):
        sys.exit()



sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(Sign_in(name='signin'))
sm.add_widget(After_login(name='afterlogin'))
sm.add_widget(Create_task(name='createtask'))
sm.add_widget(Read_task(name='readtask'))
sm.add_widget(Sign_up(name='signup'))
sm.add_widget(ExitScreen(name='exit'))


class MyApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


MyApp().run()
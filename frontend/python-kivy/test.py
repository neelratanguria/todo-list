import json
from re import MULTILINE
from tkinter import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


from todocore.reqs.sign_up import sign_up


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()

        self.inside.cols = 2
        
        self.inside.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text = "email-id: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text = "password: "))
        self.password = TextInput(multiline = False)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside)

        self.login = Button(text = "login", font_size= 40)
        self.login.bind(on_press = self.pressed)
        self.add_widget(self.login)
    
    def pressed (self, instance):
        name = self.name.text
        email = self.email.text
        password = self.password.text

        status, id = sign_up(email, password)
        
        if status:
            user_id = id
            
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump({"logged_in": True, "objectId" : user_id}, f, ensure_ascii=False, indent=4)
        else:
            print("Invalid sign up")

        #print ("name:", name,)

        self.name.text = ""
        self.email.text = "" 
        self.password.text = ""
        
class TestApp(App):
    def build(self):
        return Button(text='Hello World')
    
    def build (self):
        return MyGrid()

TestApp().run()
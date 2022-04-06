from re import MULTILINE
from tkinter import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        self.add_widget(Label(text = "email-id: "))
        self.email = TextInput(multiline = False)
        self.add_widget(self.email)

        self.add_widget(Label(text = "password: "))
        self.password = TextInput(multiline = False)
        self.add_widget(self.password)

        self.login = Button(text = "login", font_size= 40)
        self.add_widget(self.login)
    
        
class TestApp(App):
    def build(self):
        return Button(text='Hello World')
    
    def build (self):
        return MyGrid()

TestApp().run()
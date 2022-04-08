from re import MULTILINE
from ssl import _PasswordType
from tkinter import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectPoperty

class MyGrid(Widget):
    pass
    

        
class MyApp(App):
    def build(self):
        return MyGrid()
    
    
if __name__=="__main__":
    MyApp().run()
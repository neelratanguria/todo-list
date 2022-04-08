import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

class MyGrid(Widget):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def btn(self):
        print("email:", self.email.text, "password:", self.password.text)
        self.email.text = ""
        self.password.text = ""




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
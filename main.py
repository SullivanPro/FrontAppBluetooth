from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
import json

class MainPage(Screen):
    pass

class ClientPage(Screen):
    def got_json(req):
        result = UrlRequest('https://jsonplaceholder.typicode.com/posts')
        bit = json.loads(result)
        #(bit["time"]["updated"])
        return bit

    #testlol = got_json()

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("myapp.kv")

class MyApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    MyApp().run()


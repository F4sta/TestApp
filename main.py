import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import randint

kivy.require("1.9.0")

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def function(self):
        self.random_label.text = str(randint(0, 99999))

class app(App):

    def build(self):
        return MyRoot()

app = app()
app.run()

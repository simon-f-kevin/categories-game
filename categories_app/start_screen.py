from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class StartScreen(BoxLayout):
    def __init__(self, **kwargs):
        pass

    def show_button(self):
        return Button(text="Start")

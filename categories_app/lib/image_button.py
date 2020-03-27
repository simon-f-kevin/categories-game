from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class StartImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.started = False

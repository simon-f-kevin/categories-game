from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from categories_app.lib.image_button import StartImageButton

import random


class StartScreen(GridLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.letter_label = None
        self.timer_label = None
        self.timer = None
        self.seconds = 60
        self.image_button = None
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                         'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö']

    def _get_letter(self):
        result = random.choice(self.alphabet)
        print(result)
        return result

    def start_timer(self, *args):
        random_letter = self._get_letter()
        self.letter_label.text = random_letter
        self.timer = Clock.schedule_interval(self.clock_callback, 1)

    def start_timer_button_press(self, event):
        if event.started is False:
            Clock.schedule_once(self.start_timer, 3)
            event.started = True
            self.image_button.source = 'categories_app/assets/stop_button.png'
        elif event.started is True:
            self.reset_clock()
            event.started = False
            self.image_button.source = 'categories_app/assets/start_button.png'

    def clock_callback(self, *args):
        self.seconds -= 1
        val = str(self.seconds)
        if self.seconds < 10:
            val = '0' + str(val)
        if self.seconds == 0:
            self.timer_label.text = 'Time out!'
        self.timer_label.text = '00:00:{}'.format(val)

    def reset_clock(self):
        self.timer.cancel()
        self.seconds = 60
        self.timer_label.text = '00:01:00'
        self.letter_label.text = 'Press Start for a random letter'

    def display(self):
        box = BoxLayout(orientation='vertical')
        self.letter_label = l_label = Label(
            text='Press Start for a random letter', size_hint_y=(.5, .5))
        box.add_widget(l_label)
        self.image_button = StartImageButton(
            source='categories_app/assets/start_button.png',
            size_hint_x=(0.5),
            size_hint_y=(0.5, 0.5),
            center_x=0.5)
        self.image_button.bind(on_press=self.start_timer_button_press)
        box.add_widget(self.image_button)
        self.timer_label = t_label = Label(text='00:01:00',
                                           size_hint_y=(0.5, 0.5))
        box.add_widget(t_label)
        return box

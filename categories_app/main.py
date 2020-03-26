from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock
# from kivy.animation import Animation

import random
import time


Builder.load_string('''
<StartScreen>:
    cols: 1
    rows: 4
    canvas.before:
        Color:
            rgba: .85, .197, .209, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')


class StartScreen(GridLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.letter_label = None
        self.timer_label = None
        self.timer = None
        self.seconds = 60
        self.cols = 1
        self.size_hint_y = 1
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
        if event.text == 'Start':
            Clock.schedule_once(self.start_timer, 3)
            event.text = 'Stop'
        elif event.text == 'Stop':
            self.reset_clock()
            event.text = 'Start'

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
        # letter_button = Button(text='',
        #                        background_color=(0, 0, 1, 1),
        #                        size_hint_y=(0.5, 0.5))
        # letter_button.bind(on_press=self.letter_button_press)
        # box.add_widget(letter_button)
        start_timer_button = Button(text='Start',
                                    background_color=(0, 0, 1, 1),
                                    size_hint_y=(0.5, 0.5))
        start_timer_button.bind(on_press=self.start_timer_button_press)
        box.add_widget(start_timer_button)
        self.timer_label = t_label = Label(text='00:01:00',
                                           size_hint_y=(0.5, 0.5))
        box.add_widget(t_label)
        return box


class CategoriesApp(App):

    def build(self):
        view = StartScreen()
        return view.display()


if __name__ == '__main__':
    CategoriesApp().run()

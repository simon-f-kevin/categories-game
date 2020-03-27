from kivy.app import App
from categories_app.start_screen import StartScreen
from kivy.core.window import Window
import kivy.utils as utils
Window.clearcolor = utils.get_color_from_hex('#019098')


class CategoriesApp(App):

    def build(self):
        view = StartScreen()
        return view.display()


if __name__ == '__main__':
    CategoriesApp().run()

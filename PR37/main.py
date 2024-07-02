from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')  # Полноэкранный режим

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line
from random import random

class MyPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.current_color = (1, 0, 0)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.current_color)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def set_color(self, color):
        self.current_color = color

class MyPaintApp(App):
    def build(self):
        parent = BoxLayout(orientation='vertical')
        self.painter = MyPaintWidget()

        button_layout = BoxLayout(size_hint_y=None, height=70)

        clearbtn = Button(text='Clear', size_hint=(None, None), size=(70, 70))
        clearbtn.bind(on_release=self.clear_canvas)
        button_layout.add_widget(clearbtn)

        colors = [

            (1, 0, 0),
            (1, 0.5, 0),
            (1, 1, 0),
            (0, 1, 0),
            (0, 1, 1),
            (0, 0, 1),
            (0.5, 0, 0.5),
        ]

        for color in colors:
            colorbtn = Button(background_color=color, size_hint=(None, None), size=(70, 70))
            colorbtn.bind(on_release=lambda btn, col=color: self.painter.set_color(col))
            button_layout.add_widget(colorbtn)

        parent.add_widget(button_layout)
        parent.add_widget(self.painter)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):

    def build(self):
        self.expression = ""


        Window.size = (450, 650)
        Window.clearcolor = (1, 0.75, 0.8, 1)

        layout = GridLayout(cols=1, padding=10, spacing=10)

        self.label = TextInput(
            text="0",
            font_size=48,
            size_hint_y=None,
            height=100,
            halign='right',
            readonly=True,
            background_color=(1, 0.5, 0.7, 1),  # Розовый фон
            foreground_color=(1, 1, 1, 1)  # Белый текст на розовом фоне
        )
        layout.add_widget(self.label)

        # Макет сетки для кнопок
        button_layout = GridLayout(cols=4, spacing=10)

        # Кнопки указываются строка за строкой
        buttons = [
            ['1', '2', '3', 'C'],
            ['4', '5', '6', '*'],
            ['7', '8', '9', '-'],
            ['.', '0', '+', '='],
            ['(', ')', '/']
        ]

        for row in buttons:
            for button in row:
                if button == 'C':
                    button_layout.add_widget(Button(
                        text=button,
                        font_size=32,
                        background_color=(1, 0.2, 0.5, 1),  # Розовый фон кнопки "C"
                        color=(1, 1, 1, 1),  # Белый текст на кнопке
                        on_press=self.on_button_press
                    ))
                else:
                    button_layout.add_widget(Button(
                        text=button,
                        font_size=32,
                        background_color=(1, 0.6, 0.8, 1),  # Розовый фон остальных кнопок
                        color=(1, 1, 1, 1),  # Белый текст на кнопках
                        on_press=self.on_button_press
                    ))

        layout.add_widget(button_layout)

        return layout

    def on_button_press(self, instance):
        if instance.text == 'C':
            self.expression = ""
            self.label.text = "0"
        elif instance.text == '=':
            try:
                self.label.text = str(eval(self.expression))
            except Exception as e:
                self.label.text = "Error"
            self.expression = ""
        else:
            if self.label.text == "0":
                self.label.text = ""
            self.expression += instance.text
            self.label.text = self.expression

if __name__ == "__main__":
    CalculatorApp().run()

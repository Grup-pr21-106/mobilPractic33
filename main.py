from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.utils import get_color_from_hex

from kivy.config import Config


class myApp(App):
    def build(self):
        s = Scatter()
        self.st = GridLayout(size=(360, 800), cols=1)
        s.add_widget(self.st)

        self.lb = Label(text='red')
        self.st.add_widget(self.lb)

        self.tx = TextInput(text='#FF0000', halign='center')
        self.st.add_widget(self.tx)

        self.gen_button('#FF0000', 'red')
        self.gen_button('#FF8800', 'orange')
        self.gen_button('#FFFF00', 'yellow')
        self.gen_button('#00FF00', 'green')
        self.gen_button('#00FFFF', 'lightblue')
        self.gen_button('#0000FF', 'blue')
        self.gen_button('#FF00FF', 'puple')

        return s

    def gen_button(self, color_hex, color_name):
        btn = Button(
            background_color=get_color_from_hex(color_hex),
            background_normal='',
        )
        btn.fbind('on_press', self.btn_press, color_name, color_hex)
        self.st.add_widget(btn)

    def btn_press(self, color_name, color_hex, instance):
        self.tx.text = color_hex
        self.lb.text = color_name


if __name__ == "__main__":
    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '800')
    Config.write()
    myApp().run()

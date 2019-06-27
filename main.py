from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')


class CalculatorApp(App):
    def update_label(self):
        self.lb1.text = self.formula

    def addnumber(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def addoperation(self, instance):
        if str(instance.text).lower() == 'x':
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calcresults(self, instance):
        self.lb1.text = str(eval(self.lb1.text))
        self.formula = '0'

    def build(self):
        self.formula = "0"
        b1 = BoxLayout(orientation='vertical', padding=25)
        g1 = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.lb1 = Label(text='0', font_size=40,  halign='right', valign='center', size_hint=(1, .4), text_size=(400-50, 500* .4-50))
        b1.add_widget(self.lb1)

        g1.add_widget(Button(text="7", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="8", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="9", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="x", on_press = self.addoperation,
                             background_color=[1, 0, 0, 1]))

        g1.add_widget(Button(text="4", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="5", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="6", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="-", on_press = self.addoperation,
                             background_color=[1, 0, 0, 1]))

        g1.add_widget(Button(text="1", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="2", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="3", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="+", on_press = self.addoperation,
                             background_color=[1, 0, 0, 1]))

        g1.add_widget(Widget())
        g1.add_widget(Button(text="0", on_press = self.addnumber,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text=",", on_press = self.addoperation,
                             background_color=[1, 0, 0, 1]))
        g1.add_widget(Button(text="=", on_press = self.calcresults,
                             background_color=[1, 0, 0, 1]))
        b1.add_widget(g1)
        return b1
if __name__ == "__main__":
    CalculatorApp().run()

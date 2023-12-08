
# імопрт бібліотек
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *
from timer import Timer
window.clearcolor = (.33, .65, .83, 1)
lbl_color = (31, .199, .224, 1)
btn_color = (.337, .50, .23, 1)

name = ""
age = 0
p1 = 0
p2 = 0
p3 = 0



# основний клас
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        instr = Label(text=txt_instruction, color=(31, .199, .224, 1), bold=True)
        lbl_name = Label(text="Введіть ім'я:", halign='right', color=(31, .199, .224, 1), bold=True, font_size=40)
        self.input_name = TextInput(text="Микола", multiline=False)
        lbl_age = Label(text="Введіть вік:", halign='right', color=(31, .199, .224, 1), bold=True, font_size=40)
        self.input_name(text="7+", multiline=False)
        self.btn = Button(text="Почати", size_hint=(.3, .2), pos_hint={'centre_x': .5}, bold=True, background_color=r(.131, .252, .208, 1))
        self.btn.on_press = self.next
        # створення ліній
        line1 = BoxLayout(size_hint(.8, None), height="30sp")
        line2 = BoxLayout(size_hint(.8, None), height="30sp")
        # додавання віджетів на лінії
        line1.add_widget(lbl_name)
        line1.add_widget(self.input_name)

        line2.add_widget(age_name)
        line2.add_widget(self.input_name)
        # створення головної лінії і накладанняя на неї інших
        c
        main_line.add_widget(self.btn)

        self.add_widget(main_line)
    # функція для переходу на наступне вікно
    def next(self):
        global name, age
        name = self.input_name.text
        age = check_int(self.input_age.text)
        if age <= 7 or age is false:
            age = 0
            self.input_age.text = str(age)
        else:
            self.manager.current = 'second'


# різні класи(до першого вікна)
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        self.next_screen = False
        instr = Label(text=txt_test1, color=lbl_color, bold=True)


        self.lbl_sec = Timer(15, color=lbl_color, bold=True)
        lbl_result = Label(text="Введіть результат: ", halign="right", color=lbl_color, bold=True)
        self.input_result = TextInput(text="1", multiline=False)
        self.input_result.set_disabled(False)
        self.btn = Button(text="Почати", size_hint=(.3, .2), pos_hint={'centre_x': .5}, bold=True, background_color=r(.131, .252, .208, 1))
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation="vertical", padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(self.lbl_sec)
        line = BoxLayout(size_hint=(.8, None), height="30sp")
        line.add_widge(line)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

def next(self):
    global p1
    if not self.next_screen:
        self.input_result.set_disabled(False)
        self.lbl_sec.start()
    else:
        p1 = check_int(self.input_result.text)
        if p1 <=1 or p1 is false:
            p1 = 0
            self.input_result.text() = str(p1)
        else: 
            self.manager.current = 'third'

# клас до 2 вікна
class SitsScr(Screen):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        instr = Label(text=txt_sits, color=lbl_color, bold=True)

        self.sits = Label(text="Залишилось приссідань: 30", color=lbl_color, bold=True)
        self.btn = Button(text="Почати", size_hint=(.3, .2), pos_hint={'centre_x': .5}, bold=True, background_color=r(.131, .252, .208, 1))
        self.btn.on_press = self.next


        main_line = BoxLayout(orientation="vertical", padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(self.lbl_sec)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'fourth'




# клас до 3 вікна
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        instr = Label(text=txt_sits, color=lbl_color, bold=True)
        lbl_pulse = Label(text="Рахуйте пульс", color=lbl_color, bold=True)
        
        lbl_result = Label(text = "Результат:", halign = "right", color = lbl_color, bold = True, font_size = 40)
        self.input_result = TextInput(text = "0", multiline = False)
        lbl_after_res = Label(text = "Результат після відпочинку:", halign = "right", color = lbl_color, bold = True, font_size = 40)
        self.input_after_res = TextInput(text = "0", multiline = False)
        self.btn = Button(text="Почати", size_hint=(.3, .2), pos_hint={'centre_x': .5}, bold=True, background_color=r(.131, .252, .208, 1))
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation="vertical", padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(self.lbl_pulse)
        main_line.add_widget(self.lbl_sec)

        line1 = BoxLayout(size_hint(.8, None), height="30sp")
        line2 = BoxLayout(size_hint(.8, None), height="30sp")
        line1.add_widget(lbl_result)
        line1.add_widget(self.input_result)
        line2.add_widget(lbl_after_res)
        line2.add_widget(self.lbl_after_res)

        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line(self.btn)



    # функція для переходу на наступне вікно
    def next(self):
        self.manager.current = 'fifth'
# для 4 вікна
class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text="Ваш індекс Руфʼє:-14.8")
        self.index = Label(text="Працездатність серця: висока")
        main_line = BoxLayout(orientation="vertical", size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .5})
        main_line.add_widget(self.instr)
        main_line.add_widget(self.index)
        self.add_widget(main_line)

# для 5
class HeartCheck(App):
    def build(self):
        sm = ScreenManager
        sm.add_widget(InstrScr(name="first"))
        sm.add_widget(PulseScr(name="second"))
        sm.add_widget(SitsScr(name="third"))
        sm.add_widget(PulseScr2(name="fourth"))
        sm.add_widget(ResultScr(name="fifth"))
        return sm
# запуск програми
app = HeartCheck()
app.run()






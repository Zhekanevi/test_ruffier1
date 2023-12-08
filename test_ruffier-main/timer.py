from kivy.uix.label import Label
from kivy.uix.label import Clock
from kivy.uix.label import BooleanProperty



class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, **kwargs):
        self.done(False)
        self.total = total # кількість секунд в таймері
        self.current = 0 # лічильник секунд
        my_text = "Пройшло секунд: " + str(current) # текст віджету таймер
        super().__init__(text=my_text) # виклик конструктора супер класу


    def start(self): # метод запуску таймеру
        Clock.schedule_interval(self.change, 1) # запуск методу self.change кожну секунду


    def change(self, dt): # функція обробник 
        self.current +=  # збільшуємо секунди
        my_text = "Пройшло секунд: " + str(current) #  міняємо текст
        super().__init__(text=my_text)
        self.done(True)
        if self.current == self.total: # умова зупинки таймеру
            self.done = True # міняємо властивість
            return False # зупиняємо таймер






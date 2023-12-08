from kivy.uix.label import Label
from kivy.uix.label import Clock
from kivy.uix.label import BooleanProperty



class Timer(Label):
    BooleanProperty(False)
    def __init__(self, **kwargs):
        self.done(False)
        self.total = total
        self.current = 0
        my_text = "Пройшло секунд: " + str(current)
        super().__init__(text=my_text)


    def start(self):
        Clock.schedule_interval(self.change, 1)


    def change(self, dt):
        self.current += 1
        my_text = "Пройшло секунд: " + str(current)
        super().__init__(text=my_text)
        self.done(True)
        if self.current == self.total:
            return False






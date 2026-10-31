from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import random
W, H = Window.width, Window.height
class CarGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.car_w, self.car_h = W*0.18, H*0.15
        self.car_x = W/2 - self.car_w/2
        self.car_y = H*0.1
        self.enemy_w, self.enemy_h = W*0.18, H*0.15
        self.enemy_x = random.randint(0, int(W-self.enemy_w))
        self.enemy_y = H
        self.speed = 8
        Clock.schedule_interval(self.update, 1/60)
    def on_touch_down(self, touch):
        self.car_x += -70 if touch.x < W/2 else 70
        self.car_x = max(0, min(W-self.car_w, self.car_x))
    def update(self, dt):
        self.enemy_y -= self.speed
        if self.enemy_y < -self.enemy_h:
            self.enemy_y = H
            self.enemy_x = random.randint(0, int(W-self.enemy_w))
            self.speed += 0.3
        self.canvas.clear()
        with self.canvas:
            Color(0.2,0.2,0.2,1)
            Rectangle(pos=(0,0), size=(W,H))
            Color(1,1,1,1)
            for y in range(0,int(H),100):
                Rectangle(pos=(W/2-5,y), size=(10,50))
            Color(0,0.6,1,1)
            Rectangle(pos=(self.car_x,self.car_y), size=(self.car_w,self.car_h))
            Color(1,0.2,0.2,1)
            Rectangle(pos=(self.enemy_x,self.enemy_y), size=(self.enemy_w,self.enemy_h))
class CarApp(App):
    def build(self):
        return CarGame()
CarApp().run()

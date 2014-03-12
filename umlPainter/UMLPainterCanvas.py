'''
Created on Mar 2, 2014

@author: mihailo
'''
import kivy
from kivy.graphics import Color, Rectangle, Point, GraphicException
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from math import sqrt


kivy.require('1.8.0')

# Klasa predstavlja canvas na kome ce se crtati
class UMLPainterCanvas(BoxLayout):
    #konstuktor
    def __init__(self):
        super(self.__class__, self).__init__()
        
    
    def on_touch_up(self, touch):
        with self.canvas:
            print("Podigo si prst")
            return True
         
    def on_touch_move(self, touch):
        with self.canvas:
            print("Pomerio si prst")
            return True
    def on_touch_down(self, touch):
        with self.canvas:
            print("Spustio si prst")
            return True
    def metoda(self):
        print("Usao u metodu")

      
#metoda za racunanje tacaka - nalazi se van klase       
def calculate_points(x1, y1, x2, y2, steps=5):
    dx = x2 - x1
    dy = y2 - y1
    dist = sqrt(dx * dx + dy * dy)
    if dist < steps:
        return None
    o = []
    m = dist / steps
    for i in range(1, int(m)):
        mi = i / m
        lastx = x1 + dx * mi
        lasty = y1 + dy * mi
        o.extend([lastx, lasty])
    return o


        
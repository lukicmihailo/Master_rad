'''
Created on Mar 2, 2014

@author: mihailo
'''
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


kivy.require('1.8.0')


# Klasa predstavlja canvas na kome ce se crtati
class UMLPainterCanvas(BoxLayout):
    #konstuktor
    def __init__(self):
        super(self.__class__, self).__init__()
        
    
    def metoda1(self):
        
        print("Kliknuo si na dugme 1")
        return True
        
    def metoda2(self):
        print("Kliknuo si na dugme 2")
        return True
    
    def metoda3(self):
        print("Kliknuo si na dugme 3")
        return True
    
    def metoda4(self):
        print("Kliknuo si na dugme 4")
        return True
    
    def metoda(self,touch):
        with self.canvas.before:
            floatLayout = self.ids["canvasID"]
            if floatLayout.collide_point(touch.x, touch.y) == True:
                print("Kliknuo si na canvas")
                return True

   


      


        
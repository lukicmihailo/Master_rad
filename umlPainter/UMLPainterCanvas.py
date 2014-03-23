'''
Created on Mar 2, 2014

@author: mihailo
'''
import kivy
from kivy.uix.boxlayout import BoxLayout




kivy.require('1.8.0')

# Klasa predstavlja canvas na kome ce se crtati
class UMLPainterCanvas(BoxLayout):
    #konstuktor
    def __init__(self):
        super(self.__class__, self).__init__()
        
    
    def metoda1(self):
        
        print("Kliknuo si na dugme 1")
        
    def metoda2(self):
        print("Kliknuo si na dugme 2")
        
    
    def metoda3(self):
        print("Kliknuo si na dugme 3")
        
    
    def metoda4(self):
        print("Kliknuo si na dugme 4")
        

    def metoda(self):
        print("Kliknuo si na canvas")

      


        
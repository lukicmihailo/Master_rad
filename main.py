'''
Created on Feb 22, 2014

@author: mihailo
'''
#!/usr/bin/kivy
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Point, GraphicException
from random import random
from math import sqrt

class UMLPainter(App):
    title = 'UMLPainter'

    def build(self):
	print("Hello world")
        return True

    def on_pause(self):
        return True
	
    def run(self):
	print("Hello world")
	return True

if __name__ == '__main__':
      UMLPainter().run()

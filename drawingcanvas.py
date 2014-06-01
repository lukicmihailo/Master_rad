'''
Created on Jun 1, 2014

@author: mihailo
'''
from kivy.uix.relativelayout import RelativeLayout

class DrawingCanvas(RelativeLayout):
    def on_children(self,instance, value):
        self.status_bar.counter = len(self.children)
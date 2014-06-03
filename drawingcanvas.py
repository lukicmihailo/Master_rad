'''
Created on Jun 1, 2014

@author: mihailo
'''
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stencilview import StencilView


class DrawingCanvas(StencilView):
    def on_children(self,instance, value):
        self.status_bar.counter = len(self.children)
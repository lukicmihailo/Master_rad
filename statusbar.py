'''
Created on Jun 1, 2014

@author: mihailo
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
class StatusBar(BoxLayout):
    counter = NumericProperty(0)
    previous_counter = 0
    
    def on_counter(self,instance, value):
        if value == 0:
            self.msg_text = "Drawing canvas cleared"
        elif value - 1 == self.__class__.previous_counter:
            self.msg_text = "Widget added"
        elif value + 1 == self.previous_counter:
            StatusBar.msg_text = "Widget removed"
        self.previous_counter = value
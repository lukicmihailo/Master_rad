'''
Created on Apr 24, 2014

@author: mihailo
'''

#!/usr/bin/kivy
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,ListProperty

class Toolbar(BoxLayout):
    group_mode = False
    translation = ListProperty(None)
    rotation = NumericProperty(0)
    scale = NumericProperty(0)
    def clear(self,instance):
        self.drawing_canvas.clear_widgets()
    def remove (self,instance):
        ds = self.drawing_canvas
        if len(ds.children) > 0:
            ds.remove_widget(ds.children[0])
    def group(self,instance,value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselect_all()
    def color(self,instance):
        pass
    def gestures(self,instance,value):
        pass
    def unselect_all(self):
        for child in self.drawing_canvas.children:
            child.unselect()
    def on_translation(self,instance,value):
        for child in self.drawing_canvas.children:
            if child.selected and not child.touched:
                child.translate(*self.translation)
    def on_rotation(self, instance, value):
        for child in self.drawing_canvas.children:
            if child.selected and not child.touched:
                child.rotation = value
    def on_scale(self, instance, value):
        for child in self.drawing_canvas.children:
            if child.selected and not child.touched:
                child.scale = value

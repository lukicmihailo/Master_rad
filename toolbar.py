'''
Created on Apr 24, 2014

@author: mihailo
'''
from kivy.uix.boxlayout import BoxLayout


class Toolbar(BoxLayout):

    group_mode = False
    
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
        for child in self.drawing_canvas.childen:
            child.unselect()
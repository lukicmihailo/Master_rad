# File name: statusbar.py
import kivy
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import os
import pickle

from toolbox import ToolUserObject


kivy.require('1.8.0')
class StatusBar(BoxLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    type = None
    def save_diagram(self, instance):
        self.type = 'Diagram'
        self.show_save()
    def save_toolbar(self, instance):
        self.type = 'Toolbar'
        self.show_save()
    def load_toolbar(self, instance):
        self.type = 'Toolbar'
        self.show_load()
        
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()
    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()
    def load(self, path, filename):
        if self.type == 'Toolbar':
            with open('toolbar.pkl', 'rb') as input:
                userToolButton = pickle.load(input)
                newObject = ToolUserObject()
                newObject.setParent(self.tool_box)
                newObject.setObject(userToolButton.userObjectPoints, userToolButton.userObjectPointsX,userToolButton.userObjectPointsY)
                self.tool_box.add_widget(newObject)
        self.dismiss_popup()
    def save(self, path, filename):
        if self.type == 'Diagram':
            filename = os.path.join(path, filename)
            filename = filename +'.png'
            ds = self.drawing_space
            ds.export_to_png(filename=filename)
        elif self.type == 'Toolbar': 
            with open('toolbar.pkl', 'wb') as output:
                for child in self.tool_box.children:
                    if isinstance(child,ToolUserObject):
                        userToolButton = UserToolbarButton()
                        userToolButton.userObjectPoints = child.userObjectPoints
                        userToolButton.userObjectPointsX = child.userObjectPointsX
                        userToolButton.userObjectPointsY = child.userObjectPointsY
                        pickle.dump(userToolButton, output, pickle.HIGHEST_PROTOCOL)
                        userToolButton = None
        self.dismiss_popup()
        self.type = None
    def dismiss_popup(self):
        self._popup.dismiss()

class UserToolbarButton(object):
    userObjectPoints = []
    userObjectPointsX = []
    userObjectPointsY = []
 
 
 
 
 
 
 
 
 
 
                  
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
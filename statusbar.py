# File name: statusbar.py
import kivy
from kivy.uix.boxlayout import BoxLayout


kivy.require('1.8.0')
class StatusBar(BoxLayout):
    def save_diagram(self, instance):
        ds = self.drawing_space
        ds.export_to_png(filename="output.png")
        

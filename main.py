'''
Created on Feb 22, 2014

@author: mihailo
'''
#!/usr/bin/kivy
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

kivy.require('1.8.0')
Builder.load_file('basicShapes.kv')
Builder.load_file('toolbox.kv')
Builder.load_file('drawingcanvas.kv')
Builder.load_file('toolbar.kv')
Builder.load_file('statusbar.kv')

class UMLPainterFrame(AnchorLayout):
    pass

class UMLPainterApp(App):
    title = 'UMLPainterApp'
    def build(self):
        return UMLPainterFrame()

if __name__ == '__main__':
    UMLPainterApp().run()
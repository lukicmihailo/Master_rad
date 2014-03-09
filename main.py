'''
Created on Feb 22, 2014

@author: mihailo
'''
#!/usr/bin/kivy
import kivy
from kivy.app import App


from umlPainter.UMLPainterCanvas import UMLPainterCanvas

kivy.require('1.8.0')

class UMLPainterApp(App):
    title = 'UMLPainterApp'

    def build(self):
        print("Ovde ide deo za kreiranje prozora")
        return UMLPainterCanvas()

if __name__ == '__main__':
    UMLPainterApp().run()
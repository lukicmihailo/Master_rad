import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

Builder.load_file('toolbox.kv')
Builder.load_file('umlpainterwidgets.kv')
Builder.load_file('drawingcanvas.kv')
Builder.load_file('toolbar.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('umlpainter.kv')

class UmlPainterManager(ScreenManager):
    pass

class UmlPainterManagerApp(App):
    def build(self):
        return UmlPainterManager()

if __name__=="__main__":
    UmlPainterManagerApp().run()

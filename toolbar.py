
import kivy
kivy.require('1.8.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty

class ToolBar(BoxLayout):
    group_mode = False
    translation = ListProperty(None)
    rotation = NumericProperty(0)
    scale = NumericProperty(0)
    def link(self,instance):
        nizSelektovanihElemenata = []
        for child in self.drawing_space.children:
            if len(nizSelektovanihElemenata)<2:
                if child.selected:
                    nizSelektovanihElemenata.append(child)
            else:
                break
        element1 = nizSelektovanihElemenata[0]
        element2 = nizSelektovanihElemenata[1]
        self.drawing_space.paint_links(element1,element2)
        self.unselect_all()
    def clear(self, instance):
        self.drawing_space.clear_widgets()
    def remove(self, instance):
        ds = self.drawing_space
        if len(ds.children) > 0:
            ds.remove_widget(ds.children[0])

    def group(self, instance, value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselect_all()

    def color(self, instance):
        self.uml_painter.manager.current = 'colorscreen'

    def gestures(self, instance, value):
        if value == 'down':
            self.drawing_space.activate()
        else:
            self.drawing_space.deactivate()

    def unselect_all(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.translate(*self.translation)

    def on_rotation(self, instance, value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.rotation = value

    def on_scale(self, instance, value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.scale = value

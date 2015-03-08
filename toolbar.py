
import kivy
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout

from toolbox import ToolFigure, ToolButton, ToolUserObject


kivy.require('1.8.0')

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
        if len(nizSelektovanihElemenata)==2:
            element1 = nizSelektovanihElemenata[0]
            element2 = nizSelektovanihElemenata[1]
            self.drawing_space.paint_links(element1,element2)
            self.unselect_all()
    def clear(self, instance):
        self.drawing_space.clear_widgets()
    def remove(self, instance):
        ds = self.drawing_space
        if len(ds.children) > 0:
            for child in ds.children:
                if child.selected:
                    links = ds.getLinksForOneElement(child)
                    if len(links) > 0:
                        for link in links:
                            ds.removeLink(link)
                    ds.remove_widget(child)

    def group(self, instance, value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselect_all()

    def color(self, instance):
        self.uml_painter.manager.current = 'colorscreen'
    def create_widget_toolbar(self,instance):
        nizSelektovanihElemenata = []
        for child in self.drawing_space.children:
            if len(nizSelektovanihElemenata)<1:
                if child.selected:
                    nizSelektovanihElemenata.append(child)
            else:
                break
        if len(nizSelektovanihElemenata)==1:
            element1 = nizSelektovanihElemenata[0]
            newObject = ToolUserObject()
            newObject.setParent(self.tool_box)
            newObject.setObject(element1.objectPoints, element1.objectPointsX,element1.objectPointsY)
            self.tool_box.add_widget(newObject)
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

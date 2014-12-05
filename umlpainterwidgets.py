
import kivy
kivy.require('1.8.0')
from kivy.uix.scatter import Scatter
from kivy.graphics import Line

class DraggableWidget(Scatter):
    def __init__(self,  **kwargs):
        self.selected = None
        self.linked = False
        self.touched = False
        self.linkedElements = []
        super(DraggableWidget, self).__init__(**kwargs)
    def addLinkElement(self,element):
        self.linkedElements.append(element)
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.touched = True
            self.select()
            super(DraggableWidget, self).on_touch_down(touch)
            return True
        return super(DraggableWidget, self).on_touch_down(touch)

    def select(self):
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0,0,self.width,self.height), dash_offset=2)

    def on_pos(self, instance, value):
        if self.selected and self.touched:
            go = self.parent.tool_bar
            go.translation = (self.center_x- self.ix, self.center_y - self.iy)
            self.ix = self.center_x
            self.iy = self.center_y
            self.parent.repaintAllLinks(self,self.linkedElements)

    def on_rotation(self, instance, value):
        if self.selected and self.touched:
            go = self.parent.tool_bar
            go.rotation = value

    def on_scale(self, instance, value):
        if self.selected and self.touched:
            go = self.parent.tool_bar
            go.scale = value

    def translate(self, x, y):
        self.center_x = self.ix = self.ix + x
        self.center_y = self.iy = self.iy + y

    def on_touch_up(self, touch):
        self.touched = False
        if self.selected:
            if not self.parent.tool_bar.group_mode:
                self.unselect()
        return super(DraggableWidget, self).on_touch_up(touch)

    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None

class StickMan(DraggableWidget):
    pass

class Link(DraggableWidget):
    def __init__(self,  **kwargs):
        self.element1 = None
        self.element2 = None
        self.widgetLink = None
        super(DraggableWidget, self).__init__(**kwargs)


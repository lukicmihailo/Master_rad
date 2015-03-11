
import kivy
from kivy.gesture import Gesture, GestureDatabase
from kivy.uix.stencilview import StencilView

from oblici import line45_str, circle_str, cross_str
from kivy.graphics import (Canvas, Translate, Fbo, ClearColor, ClearBuffers,
Scale)

kivy.require('1.8.0')

class DrawingCanvas(StencilView):

    def __init__(self, *args, **kwargs):
        super(DrawingCanvas, self).__init__()
        self.gdb = GestureDatabase()
        self.line45 = self.gdb.str_to_gesture(line45_str)
        self.circle = self.gdb.str_to_gesture(circle_str)
        self.cross = self.gdb.str_to_gesture(cross_str)
        self.line135 = self.line45.rotate(90)
        self.line225 = self.line45.rotate(180)
        self.line315 = self.line45.rotate(270)
        self.gdb.add_gesture(self.line45)
        self.gdb.add_gesture(self.line135)
        self.gdb.add_gesture(self.line225)
        self.gdb.add_gesture(self.line315)
        self.gdb.add_gesture(self.circle)
        self.gdb.add_gesture(self.cross)
        self.links = []
    def addLink(self,link):
        self.links.append(link)
    def removeLink(self,link):
        self.remove_widget(link.widgetLink)
        self.links.remove(link) 
    def getLink(self,element1, element2):
        for child in self.links:
            if ( child.element1 == element1 and child.element2 == element2 ) or ( child.element1 == element2 and child.element2 == element1 ):
                return child
        return None
    def getLinksForOneElement(self,element):
        tempLinks = []
        for child in self.links:
            if ( child.element1 == element or child.element2 == element ):
                tempLinks.append(child)
        return tempLinks            
    def activate(self):
        self.bind(on_touch_down=self.down,
                  on_touch_move=self.move,
                  on_touch_up=self.up)

    def deactivate(self):
        self.unbind(on_touch_down=self.down,
                  on_touch_move=self.move,
                  on_touch_up=self.up)

    def down(self, ds, touch):
        if self.collide_point(*touch.pos):
            self.points = [touch.pos]
            self.ix = self.fx = touch.x
            self.iy = self.fy = touch.y
        return True

    def move(self, ds, touch):
        if self.collide_point(*touch.pos):
            self.points += [touch.pos]
            self.min_and_max(touch.x, touch.y)
        return True

    def up(self, ds, touch):
        if self.collide_point(*touch.pos):
            self.points += [touch.pos]
            self.min_and_max(touch.x, touch.y)
            gesture = self.gesturize()
            recognized = self.gdb.find(gesture, minscore=0.50)
            if recognized:
                self.discriminate(recognized)
        return True

    def gesturize(self):
        gesture = Gesture()
        gesture.add_stroke(self.points)
        gesture.normalize()
        return gesture

    def min_and_max(self, x, y):
        self.ix = min(self.ix, x)
        self.iy = min(self.iy, y)
        self.fx = max(self.fx, x)
        self.fy = max(self.fy, y)

    def discriminate(self, recognized):
        if recognized[1] == self.cross: 
            self.add_stickman()
        if recognized[1] == self.circle: 
            self.add_circle()
        if recognized[1] == self.line45:
            self.add_line(self.ix,self.iy,self.fx,self.fy)
        if recognized[1] == self.line135:
            self.add_line(self.ix,self.fy,self.fx,self.iy)
        if recognized[1] == self.line225:
            self.add_line(self.fx,self.fy,self.ix,self.iy)
        if recognized[1] == self.line315:
            self.add_line(self.fx,self.iy,self.ix,self.fy)

    def add_circle(self):
        cx = (self.ix + self.fx)/2.0
        cy = (self.iy + self.fy)/2.0
        self.tool_box.tool_circle.widgetize(self, cx, cy, self.fx, self.fy)

    def add_line(self,ix,iy,fx,fy):
        self.tool_box.tool_line.widgetize(self,ix,iy,fx,fy)

    def add_stickman(self):
        cx = (self.ix + self.fx)/2.0
        cy = (self.iy + self.fy)/2.0
        self.tool_box.tool_stickman.draw(self,cx,cy)
        

    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)
        
    def repaintAllLinks(self,element1,povezaniElementi):
        for child in povezaniElementi:
            self.tool_box.tool_line.widgetizeLink(self,element1,child)
                
    def paint_links(self,element1,element2):
        self.tool_box.tool_line.widgetizeLink(self,element1,element2)
        element1.addLinkElement(element2)
        element2.addLinkElement(element1)
        

    def export_to_png(self, filename, *args):
        if self.parent is not None:
            canvas_parent_index = self.parent.canvas.indexof(self.canvas)
            self.parent.canvas.remove(self.canvas)
        fbo = Fbo(size=self.size, with_stencilbuffer=True)
        with fbo:
            ClearColor(0, 0, 0, 1)
            ClearBuffers()
            Scale(1, -1, 1)
            Translate(-self.x, -self.y - self.height, 0)
        fbo.add(self.canvas)
        fbo.draw()
        fbo.texture.save(filename, flipped=False)
        fbo.remove(self.canvas)
        if self.parent is not None:
            self.parent.canvas.insert(canvas_parent_index, self.canvas)
        return True

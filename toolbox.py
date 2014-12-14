# File name: toolbox.py
import kivy
from kivy.graphics import Line, Color, Rectangle, Point
from kivy.uix.togglebutton import ToggleButton
import math


from umlpainterwidgets import StickMan, DraggableWidget, Link


kivy.require('1.8.0')

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super(ToolButton, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        pass

class ToolFigure(ToolButton):
    def draw(self, ds, x, y):
        (self.ix, self.iy) = (x,y)
        screen_manager = self.parent.uml_painter.manager
        color_picker = screen_manager.color_picker
        with ds.canvas:
            Color(*color_picker.color)
            self.figure=self.create_figure(x,y,x+1,y+1)
        ds.bind(on_touch_move=self.update_figure)
        ds.bind(on_touch_up=self.end_figure)

    def update_figure(self, ds, touch):
        ds.canvas.remove(self.figure)
        with ds.canvas:
            self.figure = self.create_figure(self.ix, self.iy,touch.x,touch.y)

    def end_figure(self, ds, touch):
        ds.unbind(on_touch_move=self.update_figure)
        ds.unbind(on_touch_up=self.end_figure)
        ds.canvas.remove(self.figure)
        self.widgetize(ds,self.ix,self.iy,touch.x,touch.y)

    def widgetize(self,ds,ix,iy,fx,fy):
        widget = self.create_widget(ix,iy,fx,fy)
        (ix,iy) = widget.to_local(ix,iy,relative=True)
        (fx,fy) = widget.to_local(fx,fy,relative=True)
        screen_manager = self.parent.uml_painter.manager
        color_picker = screen_manager.color_picker
        widget.canvas.add(Color(*color_picker.color))
        widget.canvas.add(self.create_figure(ix,iy,fx,fy))
        ds.add_widget(widget)

    def create_figure(self,ix,iy,fx,fy):
        pass

    def create_widget(self,ix,iy,fx,fy):
        pass
    
class ToolStickman(ToolButton):
    def draw(self, ds, x, y):
        sm = StickMan(width=48, height=48)
        sm.center = (x,y)
        screen_manager = self.parent.uml_painter.manager
        color_picker = screen_manager.color_picker
        sm.canvas.before.add(Color(*color_picker.color))
        ds.add_widget(sm)
        
class ToolCircle(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(circle=[ix,iy,math.hypot(ix-fx,iy-fy)])

    def create_widget(self,ix,iy,fx,fy):
        r = math.hypot(ix-fx, iy-fy)
        pos = (ix-r, iy-r)
        size = (2*r, 2*r)
        return DraggableWidget(pos = pos, size = size)
    
class ToolLine(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(points=[ix, iy, fx, fy])

    def create_widget(self,ix,iy,fx,fy):
        pos = (min(ix, fx), min(iy, fy)) 
        size = (abs(fx-ix), abs(fy-iy))
        return DraggableWidget(pos = pos, size = size)
    def widgetizeLink(self,ds,element1,element2):
        link = ds.getLink(element1, element2)
        if link != None:
            ds.removeLink(link)
            ds.remove_widget(link.widgetLink)
        ix = element1.center_x
        iy = element1.center_y
        fx = element2.center_x
        fy = element2.center_y
        widget = self.create_widget(ix,iy,fx,fy)
        (ix,iy) = widget.to_local(ix,iy,relative=True)
        (fx,fy) = widget.to_local(fx,fy,relative=True)
        screen_manager = self.parent.uml_painter.manager
        color_picker = screen_manager.color_picker
        widget.canvas.add(Color(*color_picker.color))
        widget.canvas.add(self.create_figure(ix,iy,fx,fy))
        ds.add_widget(widget)
        link = Link()
        link.element1 = element1
        link.element2 = element2
        link.widgetLink = widget
        ds.addLink(link)

class ToolMoveCanvas(ToolFigure):
    
    def __init__(self,**kwargs):
        ToolFigure.__init__(self, **kwargs)
        self.pocetnaX = 0
        self.pocetnaY = 0
    def on_touch_down(self,touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (self.pocetnaX,self.pocetnaY) = ds.to_widget(touch.x, touch.y)
            self.startMoveCanvas(ds, self.pocetnaX, self.pocetnaY,touch)
            return True
        return super(ToolMoveCanvas,self).on_touch_down(touch)
    def startMoveCanvas(self,ds,x,y,touch):
        ds.bind(on_touch_move=self.moveCanvas)
        ds.bind(on_touch_up=self.endMoveCanvas)
    def moveCanvas(self,ds,touch):
        if ds.collide_point(touch.x, touch.y):
            with ds.canvas:
                self.izracunavanjePomeraja(touch,self.pocetnaX,self.pocetnaY,ds)
    def endMoveCanvas(self,ds,touch):
        with ds.canvas:
            self.pocetnaX = 0
            self.pocetnaY = 0
            ds.unbind(on_touch_move=self.moveCanvas)
            ds.unbind(on_touch_up=self.endMoveCanvas)
    def izracunavanjePomeraja(self,touch,pocetnaX,pocetnaY,ds):
        if pocetnaX != 0 and pocetnaY != 0:
            #Pomeranje u desno
            if pocetnaX < touch.x and pocetnaY == touch.y:
                self.pomeriElemente(3,0,ds)
            #Pomeranje u levo
            if pocetnaX > touch.x and pocetnaY == touch.y:
                self.pomeriElemente(-3,0,ds)
            #Pomeranje gore
            if pocetnaX == touch.x and pocetnaY < touch.y:
                self.pomeriElemente(0,3,ds)
            #Pomeranje dole
            if pocetnaX == touch.x and pocetnaY > touch.y:
                self.pomeriElemente(0,-3,ds)  
            #Pomeranje gore desno
            if pocetnaX < touch.x and pocetnaY < touch.y:
                self.pomeriElemente(3,3,ds)
            #Pomeranje gore levo
            if pocetnaX > touch.x and pocetnaY < touch.y:
                self.pomeriElemente(-3,3,ds)
            #Pomeranje dole desno
            if pocetnaX < touch.x and pocetnaY > touch.y:
                self.pomeriElemente(3,-3,ds)   
            #Pomeranje dole levo
            if pocetnaX > touch.x and pocetnaY > touch.y:
                self.pomeriElemente(-3,-3,ds)
            self.pocetnaX= touch.x
            self.pocetnaY = touch.y                                            
    def pomeriElemente(self,vrednostX,vrednostY,ds):
        for element in ds.children:
            (x,y) = (element.x, element.y)
            x += vrednostX
            y += vrednostY
            element.pos = (x,y)
            


  
    
    
    
        

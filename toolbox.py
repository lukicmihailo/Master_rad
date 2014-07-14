# File name: toolbox.py
import kivy
from kivy.graphics import Line, Color, Rectangle, Point
from kivy.uix.togglebutton import ToggleButton
import math


from umlpainterwidgets import StickMan, DraggableWidget


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
class ToolSimpleLine(ToggleButton):
    def on_touch_down(self,touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x,y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y,touch)
            return True
        return super(ToolSimpleLine, self).on_touch_down(touch)
    def draw(self,ds,x,y,touch):
        (self.ix, self.iy) = (x,y)
        screen_manager = self.parent.uml_painter.manager
        color_picker = screen_manager.color_picker
        with ds.canvas:
            Color(*color_picker.color)
            touch.ud['line']=self.create_figure(x,y)
            self.figure = touch.ud['line']
        ds.bind(on_touch_move=self.update_figure)
        ds.bind(on_touch_up=self.end_figure)
    def update_figure(self, ds, touch):
        with ds.canvas:
            touch.ud['line'].points += [touch.x,touch.y]
            self.figure = touch.ud['line']
    def end_figure(self, ds, touch):
        ds.unbind(on_touch_move=self.update_figure)
        ds.unbind(on_touch_up=self.end_figure)
        self.widgetize(ds,self.ix,self.iy,touch.x,touch.y)#prosledjujemo kanvas, pocetne tacke, krajnje tacke

    def widgetize(self,ds,ix,iy,fx,fy):
        widget = self.create_widget(ix,iy,fx,fy)
        (ix,iy) = widget.to_local(ix,iy,relative=True)
        (fx,fy) = widget.to_local(fx,fy,relative=True)
        screen_manager = self.parent.uml_painter.manager
        color_picker = screen_manager.color_picker
        widget.canvas.add(Color(*color_picker.color))
        widget.canvas.add(self.create_figure(ix,iy))
        ds.add_widget(widget)

    def create_figure(self,x,y):
        return Line(points=(x,y))
#ovde treba srediti da pravi kvadrat koji ce uzimati max/min vrednosti svih pointa i od njih uzimati vrednosti
    def create_widget(self,ix,iy,fx,fy):
        pos = (min(ix, fx), min(iy, fy)) 
        size = (abs(fx-ix), abs(fy-iy))
        return DraggableWidget(pos = pos, size = size)
    
    
    
    
        
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
class ToolLine(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(points=[ix, iy, fx, fy])

    def create_widget(self,ix,iy,fx,fy):
        pos = (min(ix, fx), min(iy, fy)) 
        size = (abs(fx-ix), abs(fy-iy))
        return DraggableWidget(pos = pos, size = size)

class ToolCircle(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(circle=[ix,iy,math.hypot(ix-fx,iy-fy)])

    def create_widget(self,ix,iy,fx,fy):
        r = math.hypot(ix-fx, iy-fy)
        pos = (ix-r, iy-r)
        size = (2*r, 2*r)
        return DraggableWidget(pos = pos, size = size)

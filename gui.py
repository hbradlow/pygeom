import random, math, time
import Tkinter as tk
import numpy as np

class Point2D:
    def __init__(self,position,radius=3,fill="red",outline="black"):
        self.position = position #a numpy array
        self.radius = radius
        self.fill = fill
        self.outline = outline
    def __repr__(self):
        return "<Point2D: " + str(self.position) + ">"
    def draw(self,canvas):
        canvas.create_oval( self.position[0]-self.radius,
                            self.position[1]-self.radius,
                            self.position[0]+self.radius,
                            self.position[1]+self.radius,
                            fill=self.fill,outline=self.outline)

class Line2D:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __repr__(self):
        return "<Line2D: " + str(self.start) + " -> " + str(self.end) + ">"
    def draw(self,canvas):
        canvas.create_line(self.start[0],self.start[1],self.end[0],self.end[1])

class Visualizer:
    def __init__(self,root,width,height):
        self.drawables = [] #list of drawable objects

        self.frame = tk.Frame(root)
        self.canvas = tk.Canvas(self.frame,bg="white",width=width,height=height)
        self.canvas.pack()
        self.frame.pack()
    def add_drawable(self,drawable):
        """
            Adds a drawable to the visualizer. 
        """
        self.drawables.append(drawable)
    def run(self):
        self.draw()
    def draw(self):
        self.canvas.delete(tk.ALL)
        for drawable in self.drawables:
            drawable.draw(self.canvas)

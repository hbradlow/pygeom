import Tkinter as tk
import numpy as np

from gui import *
from algorithm.convex_hull import convex_hull

root = tk.Tk()
vis = Visualizer(root,800,600)


points = []
for i in range(100):
    point = np.random.random(2)*500 + 100
    points.append(point)
    vis.add_drawable(Point2D(point,fill="red"))

c_points = convex_hull(points)
prev = None
for point in c_points:
    if prev is not None:
        vis.add_drawable(Line2D(prev,point))
    vis.add_drawable(Point2D(point,fill="green"))
    prev = point
vis.add_drawable(Line2D(c_points[-1],c_points[0]))


vis.run()
root.mainloop()

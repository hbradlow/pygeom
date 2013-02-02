import Tkinter as tk
import numpy as np

from gui import *

root = tk.Tk()
vis = Visualizer(root,800,600)

points = []
for i in range(10):
    p = np.random.random(2)*300 + 100
    points.append(p)
    vis.add_drawable(Point2D(p,fill="green"))

vis.run()

root.mainloop()

import numpy as np

def lexicographic_sort(points):
    indices = np.lexsort(zip(*points))
    return [points[i] for i in indices]

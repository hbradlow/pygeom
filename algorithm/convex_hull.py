import numpy as np
from predicate import orient_2d

def lexicographic_sort(points):
    indices = numpy.lexsort(zip(*points))
    return [points[i] for i in indices]

def jarvis_march(points):
    sorted_points = lexicographic_sort(points)
    initial_point = sorted_points[0]
    convex_points = []

    p = initial_point
    while initial_point not in convex_points:
        q = None
        for point in points:
            if point != p:
                if q and orient_2d(q,point,p)>0:
                    q = point
                else:
                    q = point
        convex_points.append(q)
        p = q
    return convex_points

def convex_hull(points):
    return jarvis_march(points)

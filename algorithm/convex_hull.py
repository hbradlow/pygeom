import numpy as np
from predicate import orient_2d
from algorithm import lexicographic_sort

def jarvis_march(points):
    """
        Implements Jarvis March. http://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    """
    sorted_points = lexicographic_sort(points)
    initial_point = sorted_points[0]
    convex_points = []

    p = initial_point
    while all((initial_point != x).any() for x in convex_points) or not convex_points:
        q = None
        for point in points:
            if (point!=p).all() and all((point != x).any() for x in convex_points):
                if q is not None and orient_2d(p,point,q)>0:
                    q = point
                elif q is None:
                    q = point
        convex_points.append(q)
        p = q
    return convex_points

def convex_hull(points):
    return jarvis_march(points)

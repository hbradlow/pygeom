import numpy as np

def orient_2d(p,q,r):
    """
        > 0 if CCW
        < 0 if CW
        = 0 if colinear
    """
    return (q[0]-p[0])*(r[1]-p[1]) - (r[0]-p[0])*(q[1]-p[1])

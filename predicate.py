import numpy as np

def orient_2d(p,q,r):
    """
        > 0 if CCW
        < 0 if CW
        = 0 if colinear
    """
    return (q[0]-p[0])*(r[1]-p[1]) - (r[0]-p[0])*(q[1]-p[1])

def intersects(seg1,seg2):
    return \
        orient_2d(seg2.start,seg2.end,seg1.start)* \
        orient_2d(seg2.start,seg2.end,seg1.end)<=0 \
        and \
        orient_2d(seg1.start,seg1.end,seg2.start)* \
        orient_2d(seg1.start,seg1.end,seg2.end)<=0

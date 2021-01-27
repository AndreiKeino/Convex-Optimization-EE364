# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:45:57 2021

@author: Andrei
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import Rectangle
plt.close('all')

def ep_cube(cube: np.ndarray, pt: np.ndarray):
    """
    function calculates the euclidian projection of point 'pt' to a cube 'cube'
    point is a vector in R^n, cube is a set of 2 * n corners, corner is a vector in R^n

ecludian projection of point to cube

https://math.stackexchange.com/questions/3390029/projecting-a-point-onto-a-hypercube    
    
    """
    ep = np.zeros(len(pt), dtype=np.double)
    for i in range(len(pt)):
        a = np.min(cube[:, i])
        # print('a = ', a)
        # print(pt )
        b = np.max(cube[:, i])
        
        if pt[i] < a:
            ep[i] = a
            
        elif a <= pt[i] <= b:
            # ep[i] = cube[i]
            pass # no need to change this coordinate
            
        elif pt[i] > b:
            ep[i] = b
        
        else:
            raise ValueError('ep_cube: cannot calculate the coordinate, something went wrong')
    return ep

def RobustLength(v0, v1):
    amax = np.amax([v0, v1])
    if np.abs(v0) == amax:
        return np.abs(v0) * np.sqrt(1 + (v1 / v0) ** 2)
    else:
      return np.abs(v1) * np.sqrt(1 + (v0 / v1) ** 2)  
        

def GetRoot(r0, z0, z1, g, max_it = 3000):
    # see https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf
    # p. 12
    n0 = r0 * z0
    s0 = z1 - 1
    s1 = 0.0 if g < 0 else RobustLength(n0, z1) - 1
    s = 0.0
    for i in range(max_it):
        s = (s0 + s1) / 2
        if(s0 == s1 or s == s1):
            break
        ratio0 = n0 / (s + r0)
        ratio1 = z1 / (s + 1)
        g = ratio0 ** 2 + ratio1 ** 2 - 1
        if g > 0:
            s0 = s
        elif g < 0:
            s1 = s
        else:
            break
    return s
    
def DistancePiontEllipse(e0, e1, y0, y1):
    # see https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf
    # p. 12
    distance = 0.0
    x0, x1 = 0.0, 0.0
    if y1 > 0:
        if y0 > 0:
            z0 = y0 / e0 
            z1 = y1 / e1
            g = z0 ** 2 + z1 ** 2 - 1
            if g != 0:
                r0 = (e0 / e1) ** 2
                sbar = GetRoot(r0, z0, z1, g)
                x0 = r0 * y0 / (sbar + r0)
                x1 = y1 / (sbar + 1)
            else: # y0 == 0
                x0 = y0
                x1 = y1
        else:
            x0 = 0
            x1 = e1
    else: # y1 == 0
        numer0 = e0 * y0
        denom0 = e0 ** 2 - e1 ** 2
        if numer0 < denom0:
            xde0 = numer0 / denom0
            x0 = e0 * xde0
            x1 = e1 * np.sqrt(1 - xde0 ** 2)
        else:
            x0 = e0
            x1 = 0
            
    return x0, x1
        
    
    

def ep_ellipse(ellipse_a_i: np.ndarray, pt: np.ndarray, tol=1e-12, max_iter=2e3):
    """
    function calculates the euclidian projection of point 'pt' to a ellipse 
    'ellipse_a_i' by bisection method, as described in 
    https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf
    point is a vector in R^2, ellipse_a_i is a set of n ellipse parameters a_i, 
    the ellipse equation is -> sum_i(x_i^2 / a_i^2) = 1
    i.e only 2D case
    
ecludian projection of point to ellipse

https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf

https://math.stackexchange.com/questions/1775174/distance-function-of-the-ellipse-in-mathbbrn

distance from point to ellipse

https://stackoverflow.com/questions/11041547/finding-the-distance-of-a-point-to-an-ellipse-wether-its-inside-or-outside-of-e
    
    """
    
    y0 = np.abs(pt[0])
    y1 = np.abs(pt[1])
    
    x0, x1 = DistancePiontEllipse(ellipse_a_i[0], ellipse_a_i[1], y0, y1)
    
    if y0 != 0:
        x0 *= np.sign(y0)
    
    if y1 != 0:
        x1 *= np.sign(y1)
    return x0, x1
    
    
    
        
    
def is_in_cube(cube: np.ndarray, pt: np.ndarray):
    """
    function checks if the point 'pt' is inside of the cube 'cube'
    point is a vector in R^n, cube is a set of 2 * n corners, corner is a vector in R^n
    """
    for i in range(len(pt)):
        a = np.min(cube[:, i])
        b = np.max(cube[:, i])
        if not a <= pt[i] <= b:
            return False
    return True

def is_in_ellipse(ellipse_a_i: np.ndarray, pt: np.ndarray):
    """
    function checks if the point 'pt' is inside of the ellipse 'ellipse_a_i'
    point is a vector in R^n, ellipse_a_i is a set of n ellipse parameters a_i, 
    the ellipse equation is -> sum_i(x_i^2 / a_i^2) = 1
    """
    return np.sum(np.square(pt / ellipse_a_i)) <= 1

# 2D cube is just an array of 4 (x_1, x_2) point coordinates
# ND cube is just an array of 2 * N (x_1, x_2, ..., x_n) point coordinates
cube1 = np.array([[1, 0], [2, 1], [1, 1], [2, 1]]) 
pt1 = np.array([0, 0]) # point is just an array of (x_1, x_2, ...) point coordinates
assert not is_in_cube(cube1, pt1) # False
assert is_in_cube(cube1, [1, 1]) # True
assert is_in_cube(cube1, [2, 1]) # True

ellip1 = np.array([1, 2])
assert is_in_ellipse(ellip1, [0, 0]) # True
assert is_in_ellipse(ellip1, [0, 2]) # True
assert not is_in_ellipse(ellip1, [1, 0.999999]) # 

ellipse1 = ellip1 # (x_1 / ellipse1[0]) ** 2 + (x_2 / ellipse1[0]) ** 2 == 1


def plot_ellipse_and_cube_2d(cube: np.ndarray, ellipse: np.ndarray, pt: np.ndarray = None, title=None):
    # https://stackoverflow.com/questions/10952060/plot-ellipse-with-matplotlib-pyplot-python
    
    #  plot bundary (x_1 / ellipse1[0]) ** 2 + (x_2 / ellipse1[0]) ** 2 == 1 
    u=0.     #x-position of the center
    v=0.    #y-position of the center
    a = ellipse[0]    # ellipse radius on the x-axis
    b = ellipse[1]    # ellipse radius on the y-axis
    
    t = np.linspace(0, 2 * np.pi, 100)
    plt.figure()
    plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
    plt.gca().set_aspect('equal', adjustable='box')
    
    if pt is not None:
        plt.plot([pt[:, 0]], [pt[:, 1]], marker='o', markersize=3, color="red")
    
    currentAxis = plt.gca()
    
    cube_bottomleft = [cube[:, 0].min(), 
                   cube[:, 1].min()]
    cube_size = [cube[:, 0].max() - cube[:, 0].min(), 
                   cube[:, 1].max() - cube[:, 1].min()]
    currentAxis.add_patch(Rectangle(cube_bottomleft, cube_size[0], cube_size[1],
                          alpha=1, lw = 2, fill=False))
    plt.grid(color='gray',linestyle='--')
    if title is None:
        title = 'Ellipse and cube'
    plt.title(title)
    plt.show()
    
def dist(pt1: np.ndarray, pt2: np.ndarray):
    """
    fubnction calculates the distance between two points
    """
    assert pt1.shape[0] == pt2.shape[0]
    assert pt1.ndim == 1 and pt2.ndim == 1
    return np.sqrt(((pt1 - pt2) ** 2).sum())
    
cube_1 = np.array([[-1/4, 2.], [1/4, -2], [15/4, 2.], [15/4, -2]])
ellipse_1 = np.array([1, np.sqrt(2)])
                   
    
# plot_ellipse_and_cube_2d(cube_1, ellipse_1, np.array([[0., 4], [1, 1]]))
# plot_ellipse_and_cube_2d(cube_1, ellipse_1, np.array([[0., 4]]))

# we should swap x, y to comply the condition e0 > e1, see page 4 of
# ttps://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf
# i.e:

cube_1 = np.array([[2., -1/4,], [-2., 1/4], [2., 15/4], [-2., 15/4]])
ellipse_1 = np.array([np.sqrt(2), 1.]) 
# plot_ellipse_and_cube_2d(cube_1, ellipse_1, np.array([[4., 0]]), 
#                         'Ellipse and cube, x, y swapped')

cb = cube_1.copy()
el = ellipse_1.copy()
el_dst = []
cb_dst = []
pt = np.array([[4., 0]])


max_iter = 36

x = None
y = None

el_pt = np.array([4., 0])

x_test, y_test = ep_cube(cb, el_pt)

# sys.exit(0)

f = []

solved = False
k = 0

for i in range(max_iter):
    print('i = ', i)
    k = i
    x_cb, y_cb = ep_cube(cb, el_pt)
    cb_pt = np.array([x_cb, y_cb])
    print('el_pt = ', el_pt, ' cb_pt = ', cb_pt)
    f.append(dist(el_pt, cb_pt))
    
    if is_in_ellipse(el, cb_pt) and is_in_cube(cb, cb_pt):
        x, y = x_cb, y_cb
        solved = True
        break
    
    x_el, y_el = ep_ellipse(el, cb_pt)
    
    el_pt = np.array([x_el, y_el])
    print('el_pt = ', el_pt, ' cb_pt = ', cb_pt)
    f.append(dist(el_pt, cb_pt))    
    
    if is_in_ellipse(el, el_pt) and is_in_cube(cb, el_pt):
        x, y = x_el, y_el
        solved = True
        break

print('solved = ', solved, ' iters = ', k, ' x = ', x, ' y = ', y)
if solved:
    f.append(0.0)

plot_ellipse_and_cube_2d(cb, el, np.array([[x, y]]), 
                         'The point lies in ellipse and cube, x, y swapped')

plt.figure()
plt.plot(np.arange(len(f)), f)
plt.xlabel('iterations')
plt.ylabel('distance')
plt.title('Euclidean distance between the current point and the distant set')
plt.show()

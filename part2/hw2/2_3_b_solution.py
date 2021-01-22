# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:45:57 2021

@author: Andrei
"""

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
        b = np.max(cube[:, i])
        
        if cube[i] < a:
            ep[i] = a
            
        elif a <= cube[i] <= b:
            ep[i] = cube[i]
            
        elif cube[i] > b:
            ep[i] = b
        
        else:
            raise ValueError('ep_cube: cannot calculate the coordinate, something wrong')
    return ep
    
    

def ep_ellipse(ellipse_a_i: np.ndarray, pt: np.ndarray):
    """
    function calculates the euclidian projection of point 'pt' to a ellipse 'ellipse_a_i'
    point is a vector in R^n, ellipse_a_i is a set of n ellipse parameters a_i, 
    the ellipse equation is -> sum_i(x_i^2 / a_i^2) = 1
    
ecludian projection of point to ellipse

https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf

https://math.stackexchange.com/questions/1775174/distance-function-of-the-ellipse-in-mathbbrn

distance from point to ellipse

https://stackoverflow.com/questions/11041547/finding-the-distance-of-a-point-to-an-ellipse-wether-its-inside-or-outside-of-e
    
    """
    pass
    
    
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


def plot_ellipse_and_cube_2d(cube: np.ndarray, ellipse: np.ndarray, pt: np.ndarray = None):
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
        plt.plot([pt[0]], [pt[1]], marker='o', markersize=3, color="red")
    
    currentAxis = plt.gca()
    
    cube_bottomleft = [cube[:, 0].min(), 
                   cube[:, 1].min()]
    cube_size = [cube[:, 0].max() - cube[:, 0].min(), 
                   cube[:, 1].max() - cube[:, 1].min()]
    currentAxis.add_patch(Rectangle(cube_bottomleft, cube_size[0], cube_size[1],
                          alpha=1, lw = 2, fill=False))
    plt.grid(color='gray',linestyle='--')
    plt.title('Ellipse and cube')
    plt.show()
    
cube_1 = np.array([[-1/4, 2.], [1/4, -2], [15/4, 2.], [15/4, -2]])
ellipse_1 = np.array([1, np.sqrt(2)])
                   
    
plot_ellipse_and_cube_2d(cube_1, ellipse_1, np.array([0., 4]))

 

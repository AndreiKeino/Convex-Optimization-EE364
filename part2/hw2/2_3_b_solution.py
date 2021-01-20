# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:45:57 2021

@author: Andrei
"""

import numpy as np

def ep_cube(cube: np.ndarray, pt: np.ndarray):
    """
    function calculates the euclidian projection of point 'pt' to a cube 'cube'
    point is a vector in R^n, cube is a set of 2 * n corners, corner is a vector in R^n
    
ecludian projection of point to ellipse
https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf

https://math.stackexchange.com/questions/1775174/distance-function-of-the-ellipse-in-mathbbrn
    
    """
    pass

def ep_ellipse(ellipse_a_i: np.ndarray, pt: np.ndarray):
    """
    function calculates the euclidian projection of point 'pt' to a ellipse 'ellipse_a_i'
    point is a vector in R^n, ellipse_a_i is a set of n ellipse parameters a_i, 
    the ellipse equation is -> sum_i(x_i^2 / a_i^2) = 1
    
ecludian projection of point to cube

https://math.stackexchange.com/questions/3390029/projecting-a-point-onto-a-hypercube    
    """
    pass
    
    
def is_in_cube(cube: np.ndarray, pt: np.ndarray):
    """
    function checks if the point 'pt' is inside of the cube 'cube'
    point is a vector in R^n, cube is a set of 2 * n corners, corner is a vector in R^n
    """
    for i in pt.shape[0]:
        if not cube[i, 0] <= pt[i] <= cube[i, 1]:
            return False
    return True
    

def is_in_ellipse(ellipse_a_i: np.ndarray, pt: np.ndarray):
    """
    function checks if the point 'pt' is inside of the ellipse 'ellipse_a_i'
    point is a vector in R^n, ellipse_a_i is a set of n ellipse parameters a_i, 
    the ellipse equation is -> sum_i(x_i^2 / a_i^2) = 1
    """
    return np.sum(np.square(pt / ellipse_a_i)) <= 1

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:36:25 2016

@author: yali

Demo:  http://cs231n.github.io/python-numpy-tutorial/#numpy-arrays
"""

import numpy as np

#a = np.array([1, 2, 3])  # Create a rank 1 array
#print a                  # Prints "[5, 2, 3]"
#print type(a)            # Prints "<type 'numpy.ndarray'>"
#print a.shape            # Prints "(3,)"
#
#b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
#print b
#print b.shape                     # Prints "(2, 3)"

a = np.zeros((2,2))     # Create an array of all zeros
a = np.ones((1,2))      # Create an array of all ones
a = np.full((2,2), 7)   # Create a constant array
a = np.eye(5)           # Create a 2x2 identity matrix
a = np.random.random((2,2)) # Create an array filled with random values
print a

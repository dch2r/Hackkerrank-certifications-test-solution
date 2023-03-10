#/*
#Rectangle:
#• The constructor for Rectangle must take two arguments that denote the lengths of the rectangle's sides.
#• The class must have an area method that returns the area of the rectangle.

#Circle:
#• The constructor for Circle must take one argument that denotes the radius of the circle.
#• The Circle class must have an area method that returns the area of the circle. To implement the area method, use a precise Pi value, preferably the constant math.pi.

#Your implementation of all the classes will be tested by a provided code stub on several input files. Each input file contains several queries, and each query constructs an object of one of the classes and prints the area of this object to the standard output with exactly 2 decimal points.

#Constraints
#• 1 <the number of queries in one test file < 105
#• 1 ≤ the value of all parameters passed to construct the obiects ≤ 103


#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length

    pass

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    pass

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()

'''
Regular Polygons: polysum

A regular polygon has 'n' number of sides. Each side has length 's'.

* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon

Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

'''

import math
def area(n,s):
    area = (0.25*n*(s**2))/(math.tan((math.pi)/n))
    return area
    
def perimeter(n,s):
    perimeter = n*s
    return perimeter
    
def polysum(n,s):
    sum = area(n,s)+(perimeter(n,s))**2
    return round(sum,4)
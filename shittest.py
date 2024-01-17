"""
We want to calculate the circumference and area of a circle
given its radius. The relevant mathematical formulas are:
 circumference = 2 ∗ π ∗ radius
"""

import math 

radius = float(input("input rad of circle at cm: "))
circ = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print (circ) 
print (area)

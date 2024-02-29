from math import *

sides = int(input("Input number of sides: "))
length = int(input("\nInput the length of a side: "))
area = (sides * length**2) / (4 * tan(pi / sides))
print(f"\nThe area of the polygon is {area}")
import math


class Circle:
	def __init__(self, r):
		self.rad = r


	def area(self):
		pi = math.pi
		return pi * self.rad**2 

radius = input("Type a radius:")
radius = float(radius)
circle = Circle(radius)
print(circle.area())



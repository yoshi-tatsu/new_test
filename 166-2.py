class Shape:
	def __init__(self, w, l):
		self.width = w
		self.len = l


	def print_size(self):
		print("{} by {}".format(self.width, self.len))


class Square(Shape):
	def area(self):
		return self.width * self.len


class Circle(Square):
	def area(self):
		pi = 3.14
		return pi * self.width**2

	
	def print_size(self):
		print("The radius is {}".format(self.width))



a_circle = Circle(20, 20)
a_circle.print_size()
print(a_circle.area())




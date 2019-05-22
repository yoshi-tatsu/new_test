class Shape:
	def __init__(self, w, l):
		self.width = w
		self.len = l


	def print_size(self):
		print("{} by {}".format(self.width, self.len))


class Square(Shape):
	def area(self):
		return self.width * self.len


a_square = Square(30, 30)
a_square.print_size()
print(a_square.area())


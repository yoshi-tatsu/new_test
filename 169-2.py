class Rectangle:
	def __init__(self, w, l):
		self.width = w
		self.len = l


	def calculate_perimeter(self):
		return self.width * 2 + self.len * 2

class Square:
	def __init__(self, w, l):
		self.width = w
		self.len = l


	def calculate_perimeter(self):
		return self.width * 4


	def change_size(self, x):
		self.width = self.width - x
		self.len = self.len -x
		print("{} by {}".format(self.width, self.len))


sq = Square(20, 20)
sq.change_size(6)

print(sq.calculate_perimeter())



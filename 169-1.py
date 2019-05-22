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


rec = Rectangle(20, 30)
sq = Square(20, 20)
print(rec.calculate_perimeter())
print(sq.calculate_perimeter())


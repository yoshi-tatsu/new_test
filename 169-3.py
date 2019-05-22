class Shape:
	def __init__(self):
		pass
	
	def what_am_i(self):
		print("I am a shape")


class Rectangle(Shape):
	def what_am_i(self):
		print("I am a Rectangle,")


class Square(Shape):
	def what_am_i(self):
		print("I am a Square.")


rec = Rectangle()
sq = Square()

rec.what_am_i()
sq.what_am_i()


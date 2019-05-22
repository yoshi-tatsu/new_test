
class Square:
	square_list = []
	
	def __init__(self, l):
		self.len = l
		self.square_list.append(l)

	
sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(30)

print(Square.square_list)


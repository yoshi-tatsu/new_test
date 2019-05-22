
class Square:
	square_list = []
	
	def __init__(self, l):
		self.len = l
		self.square_list.append((l ,l))

	
sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(30)

for i, j in Square.square_list:
	print("{} by {} by {} by {}".format(i, i, i, i ))



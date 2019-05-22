class Triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c


	def area(self):
		s = (self.a+self.b+self.c)/2
		return (s*(s-self.a)*(s-self.b)*(s-self.c))**(0.5)

tri = Triangle(5,6,3)
print(tri.area())


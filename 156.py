class Apple:
	def __init__(self, w, c, t, s):
		self.weight = w
		self.color = c
		self.taste = t
		self.scale = s
		print("Created!!")


	def show_spec(self):
		print(self.weight)
		print(self.color)
		print(self.taste)
		print(self.scale)

apple = Apple(200., "green", "sweet", "large")
apple.show_spec()


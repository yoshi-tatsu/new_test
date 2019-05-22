class Horse:
	def __init__(self, horse, rider):
		self.horse = horse
		self.rider = rider


class Rider:
	def __init__(self, name):
		self.name = name


rider = Rider("Take")
horse = Horse("Ogri", rider)

print(horse.rider.name)


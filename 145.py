pop = []
jpop = []


def collect_songs():
	song = "Type a title of a song"
	ask = "Type p or j and type q to quit"

	while True:
		genre = input(ask)
		if genre = "q":
			break

		if genre = "p":
			p = input(song)
			pop.append(p)

		if genre = "j":
			j = input(song)
			jpop.append(j)

		else:
			print("Invalid value.")

		print("pop songs: ", pop)
		print("jpop songs: ", jpop)


collect_songs()


songs = {'1':'yesterday', '2':'sakura', '3': 'castle made of sand', '4':'kimigayo'}

num = input('type a number')

if num in songs:
	song = songs[num]
	print(song)
else:
	print('No song for the number in songs')



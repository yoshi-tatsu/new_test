import os

w = input("who is your favarite musician?")

with open("musician.txt", "w") as f:
	write = f.write(w)

with open("musician.txt", "r") as f:
	print(f.read())


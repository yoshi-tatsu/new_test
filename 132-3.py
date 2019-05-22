import os
import csv

list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline='') as f:
	for row in list:
		w = csv.writer(f, delimiter=",")
		w.writerow(row)
						
with open("movies.csv", "r") as f:
	print(f.read())


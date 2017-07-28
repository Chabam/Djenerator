import random

phrase = input("Entrez une phrase (\"Tu prends t'es affaires et tu sors!\" par défaut) : ")

if phrase == "":
	phrase = "Tu prends t'es affaires et tu sors!"

splitPhrase = phrase.split(" ")
while(True):
	random.shuffle(splitPhrase)

	output = " ".join(splitPhrase)
	print(output)
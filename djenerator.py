import random

phrase = input("Entrez une phrase (\"Tu prends tes affaires et tu sors!\" par défaut) : ")

if phrase == "":
	phrase = "Tu prends tes affaires et tu sors!"

splitPhrase = phrase.split(" ")
random.shuffle(splitPhrase)

output = " ".join(splitPhrase)
print(output)

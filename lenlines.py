import sys
import codecs

mass = ['main.py', 'BotSystem.py', 'BotUser.py', 'BotAdministrator.py', 'BotHelp.py', 'config.py', 'BotFun.py', 'DataBase.py']

lines = 0
words = 0
letters = 0

totallines = 0
totalwords = 0
totalletters = 0

mass2 = []

errorArray = []

def counterLinesWordsLetters(arrayFiles):
	lines = 0
	words = 0
	letters = 0

	totallines = 0
	totalwords = 0
	totalletters = 0

	for a in mass:
		try:
			lines = 0
			words = 0
			letters = 0
			for line in open(a, encoding="utf8"):
				lines += 1
				letters += len(line)

				pos = 'out'
				for letter in line:
					if letter != ' ' and pos == 'out':
						words += 1
						pos = 'in'
					elif letter == ' ':
						pos = 'out'
			mass2.append((a, lines, words, letters))

		except Exception as e:
			errorArray.append(f'Ошибка: {e} | в файле {a}\n')

	for a in mass2:
		totallines += a[1]
		totalwords += a[2]
		totalletters += a[3]

	try:
		for a in errorArray:
			print(a)
	except Exception as e:
		raise
	return mass2
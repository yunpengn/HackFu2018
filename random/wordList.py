# Reads all the words (line-by-line) and removes the newline at the end of each line.
words = set(line.rstrip('\n') for line in open("word_list.txt"))

# Uses this set to record all words that have been entered before.
soFar = set()

# Inititates the game for the 1st round.
newWord = input("Please type a word: ")
if newWord not in words:
	print("You didn't type a word found in word_list.txt.")
	exit()
soFar.add(newWord)
lastLetter = newWord[-1:]

# Keeps playing the game until some condition breaks.
while True:
	newWord = input("Please type a word: ")
	if newWord[0] != lastLetter:
		print("You didn't type a word starting with '{:s}'.".format(lastLetter))
		break
	if newWord in soFar:
		print("You typed a word that has been typed before.")
		break
	if newWord not in words:
		print("You didn't type a word found in word_list.txt.")
		break

	# Adds the new word into the set and updates the last letter.
	soFar.add(newWord)
	lastLetter = newWord[-1:]

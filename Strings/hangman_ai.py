# NOTE: Asked by Coursera on 2/1/18

import api
import re
from collections import Counter



####### HELPER METHODS #######
# All lowercase letters able to be guessed
def getLetters(): return 'abcdefghijklmnopqrstuvwxyz'


# Returns all unmatched words from a given phraase (words with an underscore).
def getUnmatchedWords(phrase):
	res = []
	for word in phrase.split():
		if '_' in word:
			res.append(word)
	return res


####### DICTIONARY METHODS #######
# Returns a list of our all our dictionary words from dictionary.txt
# 	and a Counter (dictionary) of all commonality of each letter
def getDictionaryAndCountLetters():
	with open('dictionary.txt') as file:
		words = file.readlines()
		uppercase = getLetters().upper()

		dictionary = set()
		countLetters = Counter()

		for word in words:
			word = word.strip('\n')
			if all(uppercaseLetter not in word for uppercaseLetter in uppercase):
				for letter in word: countLetters[letter] += 1
				dictionary.add(word)

		return (dictionary, countLetters)


# Gets a list of all words that can be a candidate for this unmatched word
def getCandidateWords(dictionary, unmatchedWord):
	regexStr = unmatchedWord.replace('_', '[' + getLetters() + ']')
	lenWord = len(unmatchedWord)
	newWords = set()

	for word in dictionary:
		if len(word) == lenWord and re.match(regexStr, word):
			newWords.add(word)
	return newWords


# Filters a dictionary to only candidate words based on a given phrase
def filterDictionary(dictionary, phrase):
	# Filter the dictionary to candidate words
	unmatchedWords = getUnmatchedWords(phrase)
	newDictionary = set()
	for unmatchedWord in unmatchedWords:
		candidateWords = getCandidateWords(dictionary, unmatchedWord)
		newDictionary = newDictionary.union(candidateWords)
	return newDictionary



####### LETTER CHOOSING METHODS #######
# Chooses best letter from given phrase
def chooseBestLetter(phrase, lettersAvailable, candidateWords, countTotalLetters):
	letterOccurrence = Counter()
	for candidate in candidateWords:
		for letter in candidate:
			if letter in lettersAvailable:
				letterOccurrence[letter] += 1

	# If no letter can be chosen from the given candidate words
	if not letterOccurrence: return max(countTotalLetters, key=lambda letter: countTotalLetters[letter])

	return max(letterOccurrence, key=lambda letter: letterOccurrence[letter])


####### TRIE METHODS/CLASSES #######
# Trie node to hold the letter and possible letters to form a word
'''
class TrieNode:
	def __init__(self, letter):
		self.letter = letter
		self.children = {}
		self.isWord = False

# Build a Trie and return the root node from the given dictionary
# Return the root Trie node and a counter of the most common letters
def getTrieAndCountLetters(words):
	root = TrieNode()
	countLetters = Counter()

	for word in words:
		curr = root

		for letter in word:
			if letter not in root.children: 
				root.children[letter] = TrieNode(letter)
			curr = root.children[letter]
			countLetters[letter] += 1

		# Set the last letter node to be a word since we finished processing this word
		curr.isWord = True

	return (root, countLetters)

# Return a set of candidate words from trie
def getCandidateWordsFromTrie(root, unmatchedWord, res, currentWord):
	if len(unmatchedWord) == 0:
		if root.isWord: res.add(currentWord + root.letter)
		return
	firstLetter = unmatchedWord[0]
	if firstLetter == '_': # Test using all children here
		pass
	elif firstLetter in root.children: # DFS to this child
		pass
'''


####### GAME METHODS #######
# Returns 1 if win, 0 if lost
def playGame():
    # Show an example usage of the API.  This creates a new game and makes
    # three guesses, showing the game state response after each call.
    response = api.send_new_game_request("test@test.com")
    letters = set(c for c in getLetters())
    dictionary, countTotalLetters = getDictionaryAndCountLetters()

    while response['state'] == 'alive':
    	phrase = response['phrase']
    	print 'response = ', response

    	# Filter dictionary based on current phrase
    	candidateWords = filterDictionary(dictionary, phrase)

    	# Choose most likely letter from these candidate words
    	bestLetter = chooseBestLetter(phrase, letters, candidateWords, countTotalLetters)
    	letters.remove(bestLetter)
    	del countTotalLetters[bestLetter]

    	# print 'guessing "' + bestLetter + '"'
    	response = api.send_guess_request(response['game_key'], bestLetter)


    print 'LOST' if response['state'] == 'lost' else 'WIN'
    return 0 if response['state'] == 'lost' else 1


# Main Function
def main():
	countGames = 0
	countWins = 0
	for _ in xrange(20):
		countGames += 1
		countWins += playGame()
	print 'win pct = ', countWins / float(countGames)


if __name__ == "__main__":
    main()

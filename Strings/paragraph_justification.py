# NOTE: Asked by Coursera on 2/1/18

def splitParagraphs(paragraph, L): # [str]
	if not paragraph: return []
	words = paragraph.split()
	cnt = 0
	current_line = []
	res = []
	for word in words:
		cnt += len(word) + 1

		if cnt < L:
			current_line.append(word)
		else:
			res.append(current_line)
			cnt = len(word) + 1
			current_line = [word]
	res.append(current_line)
	return res


def generateListToLine(words, L):
	numberOfFilled = sum(len(word) for word in words)
	numberOfWords = len(words)

	# Use this ones
	numberOfSpaces = L - numberOfFilled
	numberOfAvailableSpaces = numberOfWords - 1

	if numberOfAvailableSpaces == 0:
		return words[0]

	spaceLength = numberOfSpaces // numberOfAvailableSpaces
	spaceMod = numberOfSpaces % numberOfAvailableSpaces

	spaceArray = [spaceLength] * numberOfAvailableSpaces
	for i in range(spaceMod):
		spaceArray[i] += 1
	spaceArray.append(0)

	res = ''
	for index, word in enumerate(words):
		res += word + (' ' * spaceArray[index])
	return res

def justifyText(paragraph, L):
	res = ''
	split = splitParagraphs(paragraph, L)
	for line in split[:len(split)-1]:
		lineStr = generateListToLine(line, L)
		res += lineStr + '\n'
	res += ' '.join(split[-1])
	return res


test = "Coursera provides universal access to the world's best education, partnering with top universities and organizations to offer courses online."
print justifyText(test, 50)


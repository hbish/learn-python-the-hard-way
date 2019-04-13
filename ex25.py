def break_words(stuff):
	"""THis function will break up words"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sort words"""
	return sorted(words)

def print_first_word(words):
	"""print the first word"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""print the last word"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Take sentence and sorts the words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""print first and last"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""sorts and print first and last"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
print "Choose door 1 or 2?"

door = raw_input("> ")

if door == "1":
	print "There is a giant bear here what do you do?"
	print "1. Take the cake"
	print "2. Chuck a rock at the bear"

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats you instead"
	elif bear == "2":
		print "The bear eats your lef off"
	else: print "Well, %s is probably better. Bear went away" % bear

elif door == "2":
	print "You stare into the endless abyss at"
	print "1. Blueberries"
	print "2. Clothpins"
	print "3. Undetstaning revolve what?"

	instanity = raw_input("> ")

	if instanity == "1" or instanity == "2":
		print "lol"
	else: 
		print "the shitz"

else:
	print "the hell"
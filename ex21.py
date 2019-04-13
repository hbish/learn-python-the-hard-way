def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTUPLUING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDINF %d / %d" % (a, b)
	return a / b

print "execute"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(120, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "\n\n A puzzle"
what = add(age, subtract (height, multiply(weight, divide(iq,2))))

print "what %d " % what
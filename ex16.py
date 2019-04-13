from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you dont't want that hit CTRL+C"
print "If you do want that, hit return."

raw_input("?")

print "opening file"
target = open(filename, 'w')

print "Truncating file"
target.truncate()

print "type 3 lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Writing to file"
target.write(line1)
target.write(line2)
target.write(line3)

print "closing"
target.close()
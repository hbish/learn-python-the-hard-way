from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long " % len(indata)

print "Does the output file exist? %r " % exists(to_file)
print "Ready.hit RETURN to continue or ctrl C to quiet"
raw_input()

output = open(to_file, 'w')
output.write(indata)

output.close()

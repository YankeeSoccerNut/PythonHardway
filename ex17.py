from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

infile = open(from_file)
indata = infile.read()

#here's the one line version....don't know how to close this file though
#indata = open(from_file).read()

print "The input file %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

outfile = open(to_file, 'w')
outfile.write(indata)

print "Alright, all done."

outfile.close()
infile.close()

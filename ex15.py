#argv module is available in sys...import it so we can use it
from sys import argv

# unpack the command line
script, filename = argv

#assume we have a file as the second argument (really 1st as 0 is script)
#open this file and assign it to txt
txt = open(filename)

print "Here's your file %r:" % filename

#print out the return from the txt objects read
print txt.read()

#repeat but this time get the user to type in the filename
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#close out the open files
txt.close()
txt_again.close()

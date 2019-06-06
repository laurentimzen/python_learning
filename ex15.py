from sys import argv

script, filename = argv

txt = open(filename) # opens the file the user provides

print "Here's your file %r" % filename
print txt.read() # reads through the txt file given and prints it


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again) # opens the file once more when user inputs it

print txt_again.read() # reads/prints the file once more

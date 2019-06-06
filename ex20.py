from sys import argv

# argv accepts the script and inputed file as input
script, input_file = argv

# creates function to print all of the input
def print_all(f):
    print f.read()

# create function to rewind the input and set to 0
# 0 is in bytes... the start of the file
def rewind(f):
    f.seek(0)

# reads one line at a time
def print_a_line(line_count, f):
    print line_count, f.readline()

# current files is input file
# opens it
current_file = open(input_file)

# calls print all using the current file
print "First let's print the whole file:\n"
print_all(current_file)

# calls rewind using the current file
print "Now lets rewind, kind of like a tape."
rewind(current_file)

# increases the current_line by 1 each time and prints it
# alongside the current file line
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

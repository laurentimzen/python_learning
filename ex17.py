from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

# Here's the above as a one liner
# indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does te output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

# open(to_file, 'w').write(indata)... above as one liner

print "Alright, all done."

out_file.close()
in_file.close()

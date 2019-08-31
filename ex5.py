name = 'Lauren P. Timzen'
age = 19 # the truth!
height = 64 # inches
centimeters = height * 2.54
weight = 150 # lbs
kilograms = weight / 2.205
eyes = 'Green'
teeth = 'White'
hair = 'Light brown'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky!
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight
)

print "she is %f centimeters tall" % centimeters
print "she is %f kilos heavy" % kilograms

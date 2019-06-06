def subway_stats(subs_made, tips_made):
    print "You have %d subs made!"  % subs_made
    print "You have earned %d dollar sin tips!" % tips_made
    print "You have earned %d dollars per sub" % (tips_made / subs_made)
    print "eat fresh!"

# simple arguments
subway_stats(10, 5)

# using vairables
subs_made = 20
tips_made = 10
subway_stats(subs_made, tips_made)

# doing math inside
subway_stats(10 + 20, 10 + 5)

# variables and math inside
subs_made = 5
tips_made = 10
subway_stats(subs_made * 2, tips_made + 3)

# assign function to a variable
subway = subway_stats
subway(30, 1)

# user input
print "how many subs did you make today?"
subs_made = int(raw_input('>'))
print "how many tips did you make today?"
tips_made = int(raw_input('>>'))
subway_stats(subs_made, tips_made)

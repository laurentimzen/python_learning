def call_list(x):
    num_list = []

    for i in range(0, x):
        print"At the top i is %d" % i
        num_list.append(i)

        print "Numbers now: ", num_list
        print "At the bottom i is %d" % i

call_list(5)

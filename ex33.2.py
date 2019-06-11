def call_list(x):
    num_list = []
    i = 0

    while i < x:
        print"At the top i is %d" % i
        num_list.append(i)

        i += int(raw_input(">> "))
        print "Numbers now: ", num_list
        print "At the bottom i is %d" % i

call_list(100)

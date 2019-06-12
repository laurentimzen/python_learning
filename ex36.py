from sys import exit

rooms = []


def start():
    print "you have been to the following rooms:", rooms
    print "there's a smell wafting from the north."
    print "you hear sounds to the right."
    print "to the left you see a slew of underwear."
    print "below you the ground feels hot."
    print "will you go north, right, left, or down?"

    next = raw_input(">> ")

    if next == "north":
        bathroom()
    elif next == "right":
        garage()
    elif next == "left":
        bedroom()
    elif next == "down":
        hell()
    else:
        dead("you walk straight into a wall and drop dead.")



def dead(why):
    print why, "you dumb fuck."
    exit(0)

def win():
    print "you have visited all the rooms. that's pretty cool."
    exit(0)


def bathroom():
    print "you open the door and are hit with a rancid odor."
    print "there is a huge shit sitting in the toilet."
    print "you suddenly have to use the toilet."
    print "will you: unclog or use toilet anyway?"
    unclogged = False

    while True:
        next = raw_input(">> ")

        if next == "unclog" and not unclogged:
            print "you take the plunger and unclog the toilet. P.U."
            unclogged = True
        elif next == "unclog" and unclogged:
            print "the toilet's already unclogged you dumb fuck."
            dead("the plunger attacks you for being an idiot. you're dead.")
        elif next == "use toilet anyway" and not unclogged:
            dead("the poop is angry that you're shitting on it. it pulls you in and flushes you.")
        elif next == "use toilet anyway" and unclogged:
            print "you take a nice long shit and head back to where you came from."
            rooms.append("bathroom")
            if(len(rooms) == 4):
                win()
            else:
                start()
        else:
            dead("type the right command moron. ")




def garage():

    def look():
        print "you find Tony's razor and pick it up."
        to_do.append("razor")
        print "now you just need to find tony's suit!"
        print "you see it dead ahead. pick it up?"

    to_do = []

    print "you walk into the garage and find tony stark staring at you"
    print "he says nothing at all but he hands you a list."
    print "the list reads the following: find razor, suit."
    print "find these things for tony and he will let you leave."
    print "will you look around?"

    next = raw_input(">> ")

    if next == "yes":
        print "you look around and see a table."
    else:
        dead("tony is angry that you're not doing anything and blasts your head off, ")


    print "will you look on top or under the table?"
    next = raw_input(">> ")
    if next == "on top":
        look()
    elif next == "under":
        print "you see an oil spill, but nothing else eventful."
        next = raw_input(">> ")
        if next == "on top":
            look()
        else:
            dead(nice,)
    else:
        dead("literally why can't you type, ")

    next = raw_input(">> ")
    if next == "yes":
        print "you pick up the suit and lug it over to Tony."
        to_do.append("suit")
    else:
        dead("do you even know how to follow instructions, ")

    print "you look down at your list: "
    print to_do
    print "Tony is satisfied and lets you leave."
    rooms.append("garage")
    if(len(rooms) == 4):
        win()
    else:
        start()



def hell():
    print "a chasm opens up below you and you descend into the earth"
    print "the smell of lunch meats and subway subs fills the air"
    print "you have arrived in hell"
    print "there seems to be nothing else to do except get into the sub line. will you get in line?"

    next = raw_input(">> ")
    if next == "yes":
        print "you get into the line. it's very long, but you eventually get to the front."
        print "the sandwich artist asks how many footlongs you want."
        sub = int(raw_input(">> "))
        for x in range(0, sub):
            print "why did you ask for so many subs?"
        if (sub > 4):
            dead("you shouldn't have asked for so many subs.")
        else:
            print "the subway gods bless you. you rise back up to where you came from."
            rooms.append("hell")
            if(len(rooms) == 4):
                win()
            else:
                start()
    else:
        dead("u spend eternity in hell,")



def bedroom():
    print "you walk into your own bedroom and find fat chris pratt sitting on your bed"
    print "chris pratt is staring at you"
    print "chris pratt\nwill\nnot\nlook\naway"
    print "what will you do to chris pratt?: fight or give in"

    next = raw_input(">> ")
    if next == "fight":
        print "you and chris pratt start to fight."
        print "the fight is never ending"
        dead("you spend the rest of your life wrestling chris pratt.")
    elif next == "give in":
        print "you submit yourself to chris pratt for eternity"
        print "he asks you to scrub under his folds."
        dead("you get trapped under one of chris pratt's fat folds and suffocate.")
    else:
        print "you didn't follow directions, but that was clever."
        print "you go back to wence you came."
        rooms.append("bedroom")
        if(len(rooms) == 4):
            win()
        else:
            start()



start()

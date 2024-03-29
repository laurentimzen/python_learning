from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Finish(Scene):

    def enter(self):
        exit(1)

class Death(Scene):

    quips = [
    "you died bc u suck.",
    "u kiss your mohter with that mouth?",
    "tony stark is rolling in his grave",
    "you are so stupid"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving memeber and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, and evil clown costume."
        print "He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at him."
            print "His clown costume throws off your aim."
            print "Your laser hits his costume and misses him entirely. This"
            print "makes him fly into a rage and blast you repeatedly in the face until."
            print "you are dead. Then he he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, wave, and slip and slide right."
            print "as the Gothon's blaster cranks a laser past your head"
            print "in th emiddle of your artful dodge you foot slips and you."
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know."
            print "lbe he jsflkajlf, dsfaljk, gjafksfda, ekjkfasf. jflksaj!"
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him in the head."
            print "you jump through the weapon armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeapoArmory(Scene):

    def enter(self):
        print "you dive into the weapon armory, crouch and scan the room"
        print "for more hidden gothons. it's dead quiet. too quiet."
        print "you stand up and run to the far side of the room and find the"
        print "neutron bomb in its containers. there's a keypad lock on the box"
        print "you need the code to get the bomb out. if you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. the code is 3 digits."
        code = "%d%d%d" % (2, 5, randint(1,9))
        print "if you want a cheat, press 3"
        cheat = raw_input(">  ")
        if int(cheat) == 3:
            print code
        else:
            pass
        guess = raw_input("[keypad]>  ")
        guesses = 0

        while guess != code and guesses < 9:
            print "BZZZZZZZED!!"
            guesses += 1
            guess = raw_input("[keypad]>   ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "you grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'

        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "you decide to sit there, and finally the gothons blow up the"
            print "ship from their ship and you die."
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print "you burst onto the bridge with the neutron bomb"
        print "under your arm and surprise 5 gothons who are trying to"
        print "take control of the ship. each of them has an even uglier"
        print "clown costume than the last. they haven't pulled their"
        print "weapons out yet, as they see the active bomb udner your"
        print "arm and don't want to set it off"

        action = raw_input(">  ")

        if action == "throw the bomb":
            print "in a panic you throw the bomb at the group"
            print "and make a leap for the door. right as you drop it a "
            print "gothon shoots you in the back, killing you"
            print "as you die you see another gothon try to disarm the bomb."
            print "you die knowing they will probably blow up when it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "you point your blaster at the bomb under your arm."
            print "and the gothons put their hands up and start to sweat."
            print "you inch backward to the door, open it, and carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "then you jump back through the door, pinc ht ecloes bottom"
            print "and black the lock so the gothons can't get out."
            print "now that the bomb is placed you run to the escape pod"
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"



class EscapePod(Scene):

    def enter(self):
        print "you rush through the ship trying to make it to"
        print "the escape pod before the whole ship blows. it seems like"
        print "hardly any gothons are on the ship, so your run is clear of"
        print "interference. you get to the chamber with the escape pods, and"
        print "now need to pick one to take. some of them could be damaged"
        print "but you don't have time to look. there's 9 pods."
        print "which one do you take?"
        print "if you want to know which pod to take, press 3"
        cheat = raw_input(">  ")
        good_pod = randint(1,9)

        if int(cheat) == 3:
            print good_pod
        else:
            pass

        guess = raw_input("[pod #]>  ")

        if int(guess) != good_pod:
            print "you jump into pod %s and hit the eject button" % guess
            print "the pod escapes out into the void of space, then"
            print "implodes, crushing your body into jam jelly."
            return 'death'

        else:
            print "you jump into pod %s and hit the eject button" % guess
            print "the pod slides out into space heading to"
            print "the planet below. as it flies you look back"
            print "and see your ship implode like a bright star"
            print "it takes out the gothon ship at the same time. you won!"

            return 'finished'



class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeapoArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finish()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

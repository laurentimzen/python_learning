class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit() # takes the print straight from Parent

dad.override()
son.override() # overrides the Parent by defining its own version

dad.altered()
son.altered() # overrides the Parent function altered by defining its own
              # also prints the Parent version using super

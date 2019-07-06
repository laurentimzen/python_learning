## Animal is-a object
class Animal(object):
    pass

## Class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has-a __init__ that takes self and name parameters
        self.name = name

## Class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Class Cat has-a __init__ that takes self and name parameters
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Class Person has-a __init__ that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init_ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## Class Fish is-a object
class Fish(object):
    pass

## Class Salmon is-a Fish
class Salmon(object):
    pass

## Class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## frank is-a Employee, his salary is 120000
frank = Employee("Frank", 120000)

## frank's pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

# Demonstrates private variables and methods

class Critter:
    def __init__(self, name, mood):
        print "A new critter has been born!"
        self.name = name            # public attribute
        self.__mood = mood
        # private attribute
    def __str__(self):
        return "Ends Here"
    def talk(self):
        print "\nI'm", self.name
        print "Right now I feel", self.__mood, "\n"
    def __private_method(self):
        print "This is a private method."
    def public_method(self):
        print "This is a public method."
        self.__private_method()

# main
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.public_method()
print '==',crit._Critter__mood
print dir(crit)
print "\n--->",crit._Critter__private_method()
print crit.__doc__
#Bird class               
"""
OOP classes and inheritance: 

Assertions are used to test whether the function outputs satisfy our goal.
For example, assert(type(bird1) == Bird). This means the type of bird1 should be "Bird".
Remember, whatever inside the bracket should be TRUE to pass the assertion.

Read the test case (assertions) to see what each function should do!

Parent Class:
A basic Bird has a species name, can fly, and can lay eggs
You will input a species name when creating a class object.
Fly function will output a sentence. 
CountEgg returns the egg each object has.
LayEgg will change the number of eggs each object has.
repr will return a sentence in this format "[Species] has [number of eggs]". Be careful of 1 egg and 2 eggs.(You need to satisfy both cases)

Child Class:
Penguin class inherits from Bird class.
It can't fly, but it can swim. Rewrite fly function and add swim function.

MessengerBird class inherits from Bird class.
Rewrite the init function. 
This object can either carry a message when initialized or not.

Run the file after finishing the code. If it prints "Done!", congrats!
"""
class Bird(object):
    def __init__(self,species):
        self.species = species
        self.eggs = 0

    def fly(self):
        return "I can fly!"

    def countEggs(self):
        return self.eggs
        
    def layEgg(self):
        self.eggs += 1
        
    def __repr__(self):
        if self.eggs == 1:
            return self.species + " has " + "1 egg"
        else:
            return self.species + " has " + str(self.eggs) + " eggs"
        
class Penguin(Bird):
    #inherit from Bird class
    #override method fly()
    def fly(self):
        return "No flying for me."
            
    def swim(self):
        return "I can swim!"
            
class MessengerBird(Bird):
    #inherit from Bird class
    #override init
    def __init__(self,species,message=""):
        self.species = species
        self.eggs = 0
        self.message = message
        
    def deliverMessage(self):
        return self.message
        
## helper function
def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

### Test case
def testBirdClasses():
    print("Testing Bird classes...", end='')
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")
    assert(getLocalMethods(Bird) == ['__init__', '__repr__', 'countEggs', 
                                     'fly', 'layEgg'])
    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")
    print(getLocalMethods(Penguin))
    assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))
    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")
    bird4 = MessengerBird("Homing Pigeon")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
    print("Done!")

testBirdClasses()

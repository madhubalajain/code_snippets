# Duck Typing and Easier to ask forgiveness than permission (EAFP)
# Object walk like a duck and quacks like a duck than it is duck


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")
        
 def quack_and_fly(thing):
    # Not Duck-Typed (Non-Pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
    print('This has to be a Duck!')

d = Duck()
quack_and_fly(d)

p =Person()
quack_and_fly(p)

--------------------------------------------------------
#Duck Typing - Pythonic

 def quack_and_fly(thing):
        thing.quack()
        thing.fly()
    
d = Duck()
quack_and_fly(d)

p =Person()
quack_and_fly(p)

--------------------------------------------------------
#Easier to ask forgiveness than permission - Non-Pythonic
# Look before you leave (LBYL)


 def quack_and_fly(thing):
        # LBYL (Non-Pythonic) - Asking permission at 56, 57
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
-------------------------------------------------------
# Try to do something, if it work, than fine and if not try to handle that error

def quack_and_fly(thing):
    # EAFP (Pythonic)
         try:
             thing.quack()
             thing.fly()
             thing.bark()
         except AttributeError as e:
             print(e)
   
  -------------------------------------------------------  

def quack_and_fly(thing):
    pass
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    #     try:
    #         thing.quack()
    #         thing.fly()
    #         thing.bark()
    #     except AttributeError as e:
    #         print(e)

d = Duck()

print(type(dir(d)))


----------------------------------------------------------------

person = {'name' : 'Madhu', 'age' : 25, 'job' = 'SE'}
#person = {'name' : 'Madhu', 'age' : 25}

#LBYL (Non - pythonic)

if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {} and my age {} and job is {}".format(***person))
else
    print("Missing some key")

#EAFP

try:
    print("I'm {} and my age {} and job is {}".format(***person))
except KeyError as e:
    print("Missing {} key".format(e))
    
    
    






#----------
# Introduction to OOP: 
# Inheritence and POlymorphism
#
#----------
import math 

#Creating a base class 
class Animal():

  def __init__(self):
    print('Animal Created')
  
  def who_am_i(self): 
    print("I am an animal")
  
  def eat(self):
    print("I am eatting")

#inherit or derive from base class
class Dog(Animal): 

  def __init__(self): 
    Animal.__init__(self)
    print("Doggy Created")
  #Can redefine a method by choosing the same name
  def who_am_i(self): 
    print("I am a Doggy")
  #Can add more methods, attributes, etc. 
  def bark(self):
    print("Raggy")

mydog = Dog()
mydog
mydog.who_am_i()
print('\n')

#######PART TWO#######
#######
# Polymorphism
# Sharing method name...???
#######
######################

class Doggy(): 

  def __init__(self, name): 
    self.name = name

  def speak(self):
    return self.name + " says woof"

class Pussy(): 

  def __init__(self, name): 
    self.name = name

  def speak(self):
    return self.name + " says meOW"

pica = Doggy("Pica")
felix = Pussy("Felix")

print(pica.speak())
print(felix.speak())
print('\n')

###########
#demonstrate polymorphism
#Only when sharing the same method name.
###########

for pet in [pica,felix]: 
  print(type(pet))
  print(type(pet.speak())) 
print('\n')

#define a function to be agnostic
def pet_speak(pet): 
  print(pet.speak())
pet_speak(pica)
pet_speak(felix)

print('\n')
#####True Polymorphism#####
#using abstract classes and inheritence.
########################### 
class AniMal(): 

  def __init__(self,name):
     self.name = name
  
  def speak(self):
    raise NotImplementedError("Subclass must implement this abstract method")

class Doggie(AniMal): 

  def speak(self): 
    return self.name+ " says woof!"

class Pussie(AniMal): 

  def speak(self): 
    return self.name+ " says mew!"

fido = Doggie('Fido')
isis = Pussie('Isis')

print(fido.speak())
print(isis.speak())


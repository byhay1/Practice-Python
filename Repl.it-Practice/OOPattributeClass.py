#----------
# Introduction to OOP: 
# Attributes and Class Keywords
#
#----------
import math 

mylist = [1,2,3]
myset = set()
#built in objects
type(myset)
type(list)

#######
#define a user defined object
#Classes follow CamelCasing
#######
#Do nothing sample class
class Sample(): 
  pass
#set variable to class
my_sample = Sample()
#see type using built-in object
type(my_sample)

#######
#Give a class attributes
#######
#do something Dog class
class Dog(): 
  def __init__(self,breed,name,spots):
    #Attributes
    #We take in the argument
    #Assign it using self.attribute_name 
    self.breed = breed
    self.name = name
    #Expect boolean True/False
    self.spots = spots
#because attribute is used, must pass expected attribute or it will return an error
my_dog = Dog(breed='Mutt',name='Ruby',spots=False)
#Check to see type=instance of the dog class. 
my_dog.breed
my_dog.name
my_dog.spots

#######PART TWO#######
#######
#Using Class object attribute and more... 
#Using Methods within class
#######
######################
class Doggy(): 
  # CLASS OBJECT ATTRIBUTE 
  # SAME FOR ANY INSTANCE OF A CLASS
  clss = 'mammal'
  # USER DEFINED ATTRIBUTE
  def __init__(self,breed,name):
    #Attributes
    #We take in the argument
    #Assign it using self.attribute_name 
    self.breed = breed
    self.name = name
  # OPERATIONS/Actions ---> Methods
  def bark(self, number): 
    print("WOOF! My name is {} and I am {} years old".format(self.name, number))
#because attribute is used, must pass expected attribute or it will return an error
my_dog2 = Doggy(breed='whtMutt',name='Rita')
#Methods need to be executed so they need '(' ')'
my_dog2.bark(2)


#######
#Create a new class called 'Circle'
#######
class Circle(): 
  # CLASS OBJECT ATTRIBUTE
  pi = math.pi

  def __init__(self, radius=1): 
    self.radius = radius
    self.area = radius*radius*Circle.pi
  
  # METHOD
  def get_circumference(self): 
    return self.radius*2*Circle.pi

my_circle = Circle(33)

print(my_circle.get_circumference)
print(my_circle.area)
print(my_circle.pi)




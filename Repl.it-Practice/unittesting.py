########################
#~Unit Testing~#
########################
# Basics
### - pylint:
# This is a library that looks at your code and reports back possible issues
### - unittest:
# This built-in library will alolow to test your own programs and check you are getting desired outputs
#########################

#Must install via: 
#pip install pylint

# throw an error on purpose
a = 1
b = 2 
print(a)
#print(B)

#then use pylint to grade code.
#WILL NOT WORK IN repl.it ... probably already in container
#pylint will grade this a 12.5 out of 10 

#To get a better pylint score try this

def myfunc(): 
  first = 1
  second = 2
  print(first)
  print(second)
myfunc():




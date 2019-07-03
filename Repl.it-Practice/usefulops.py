#some stuffs

#range can iterate a current list to a desired amount
mylist = [1,2,3]
for num in range(10):
  print(num)
print('\n')

#can set the starting point of a range by using this syntax
#range (START, STOP)
for num in range(3,10): 
  print(num)
print('\n')

#can also use steps - see format for slicing, it is the SAME
#range (START,STOP,STEP)
for num in range(0,11,2):
  print(num)
print('\n')

#can also cast it to a list 
#this is a GENERATOR... no clue what that is right now
list(range(0,11,2))

#-----------
#counting stuff
#enumerate stuffs... return tuple stuffsss
#-----------
indexcount = 0
word = 'abcde'
for item in enumerate(word): 
  print(item)
  indexcount += 1
# lets unpack it
for index,letter in enumerate(word):
  print(index)
  print(letter)

#-----------
#use some ZIPS
#combine list in a tuple
#-----------
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

print('\n')
for item in zip(mylist1,mylist2,mylist3):
  print(item)

#---------
# MIN and MAX functions
#---------
mylist4 = [10,20,30,40,100]
# use min 
print('\n',min(mylist4))
# use max 
print('\n',max(mylist4))

#--------
#RANDOM
#--------
#shuffle import
#---NOTE SHUFFLE and RANDOM DON'T FREAKIN WORK 
from random import shuffle
mylist5 = [1,2,3,4,5,6,7,8,9,10]
# use shuffle
print(shuffle(mylist5))

from random import randint
print(randint(0,100))

#--------
# work on INPUTS
# everything is a string
#--------

#start inputs
result = input('What is your name: ')
print(result)

#you have to cast it in order to change from string to what you want
result2 = input('How old are you: ')
int(result2)
compage = 50 - int(result2)
compage2 = int(result2) - 50
print(int(result2))
int(result2)

if int(result2) <= 49: 
  print('I am ',compage,'older than you!')
elif int(result2) == 50:
  print('we are the same age')
else: 
  print('you are ', compage2, 'older than me! TF')
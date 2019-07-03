#---------
#Test Python knowledge of functions and methods
#---------

#Write a function that computes the volume of a sphere given its radius
import math 
rad = 2

def vol(rad):
  vol = (4.0/3)*math.pi*(rad**3)
  return vol

print(vol(rad))
print('\n')

#Write a function that checks whether a number is in a given range (Inclusive of high and low)
num = int(input('Enter a number: '))
low = int(input('Enter a low number: '))
high = int(input('Enter a high number: '))

def ran_check(num,low,high):
  if num in range(low,high): 
    print("This number is in range!")
  else: 
    print("Sorry out of range")

ran_check(num,low,high)
print('\n')

#Write a function that checks whether a number is in a given range (Inclusive of high and low) BUT BOOLEAN RESULTS
num = int(input('Enter a number: '))
low = int(input('Enter a low number: '))
high = int(input('Enter a high number: '))

def ran_check2(num,low,high):
  if num in range(low,high): 
    return True
  else: 
    return False

print(ran_check2(num,low,high))

#OR

def ran_check3(num,low,hight): 
  return num in range(low,high)

#Write a python function that accepts a string and calculates the number of upper case letters and lower case letters. 

s = 'Hi, this is Bob. Bob has totally LOST his mind!'

def up_low(s): 
  d = {"upper":0, "lower":0}
  for letter in list(s): 
    if letter.isupper():
      d["upper"]+=1 
    elif letter.islower():
      d["lower"]+=1
    else: 
      pass  
  print('',"Original String: ", s, '\n', "No. of Upper case characters: ", d["upper"], '\n', "No. of Lower case characters: ", d["lower"])

up_low(s)
print('\n')

#Write a Python function that takes a list and returns a new list with unique elements of the firt list

sl = [1,1,1,1,2,2,3,3,3,3,4,5]
ul = [1,2,3,4,5]

def unique_list(l): 
  x = []
  for n in l: 
    if n not in x: 
      x.append(n)
  return x
  
print(unique_list(sl))

#Write a Python function to multipy all the numbers in a list
sn = [2,2,2,2]
def multiply(numbers): 
  total = 1 
  for x in numbers: 
    total *= x
  return total 

print(multiply(sn))



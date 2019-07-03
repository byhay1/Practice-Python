#---------------
#Methods and Functions!
#--------
# Start with METHODS
#----------------

#methods in built-in objects
mylist = [1,2,3]

#1) .append to add to  a list
mylist.append(4)


#2) .pop to remove last item on the list
mylist.pop()

#3) other methods [.clear, .copy, .count, .extend, .index]...
#[.insert, .remove, .reverse, .sort]
#if you need help with this call the built-in help function
#syntax help(variable.method)

######print(help(mylist.insert))

#---------------------------------------

#-----------------
#FUNCTIONS
#---------
#syntax
# def name_of_function():
#   '''
#   docstring explains function
#   '''
#   print("Hello") OR return
#>> name_of_function
#>> Hello
#
#syntax
# def add_function(num1,num2):
#   return num1+num2
# NOTE: to find all defined functions in command prompt use the dir() command
#------------------

#basic function
def namefun():
  '''
  stuff
  '''
  return 'Hello'

print(namefun())

#take in parameters
def say_hello(name=''):
  return 'Hello ' + name

print(say_hello('Byron'))

#take in two parameters
def addstuff(n1,n2): 
  return n1 + n2

print(addstuff(2,6))

#--------
#complex functions
#--------

#find out if the word dog is in a string
def dog_check(mystring):
  if 'dog' in mystring.lower(): 
    return true
  else: 
    return false
# or do this...
def dog_check2(mystring):
  return 'dog' in mystring.lower()
print('\n')
print(dog_check2('Snoop doggy dog'))
print(dog_check2('I hate kitty cats'), '\n')

#----------------
#more complex functions
#--------
# PIG LATIN
#
# If word starts with a vowel.add 'ay' to end
# If word does not start with a vowel, put first letter at the end , then add 'ay'
# word --> ordway
# apple --> appleay
#-----------------

def piglatin(word):
  
  first_letter = word[0]
  #check if vowel
  if first_letter in 'aeiou':
    pig_word = word + 'ay'
  else: 
    pig_word = word[1:] + first_letter + 'ay'

  return pig_word

print(piglatin('word'))
print(piglatin('igloo'))

#-------------
#-------------------
#Function Parameters continued!
#*args
#**kwargs
#-------------------
#-------------
print('\n')
def myfunc2(a,b):
  #returns %5 of the sum of a and b
  return sum((a,b)) * 0.05

#use *arg for an arbitrary num of arguments
#pass as many parameters as you want through a tuple
def myfunc3(*args):
  return sum(args) * 0.05

#use **kwargs to create a key value pair OR dictionary
'''
def myfunc4(**kwargs): 
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('I did not find the fruit here')
myfunc4(fruit = 'apple', veggie = 'Potato')
'''
#----------
'''
def myfunc5(*args,**kwargs): 
  print(args)
  print(kwarg)
  print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc5(10,20,30,fruit='orange',food='eggs',animal='dog')
'''
#----------

#---PRACTICE---
#check if the lesser of two evens true then print the lesser of two evens, else print greater odd number
def lesser_of_two_evens(a,b):
  if a%2 == 0 and b%2 == 0: 
    #Both numbers are even
    if a < b: 
      result = a
    else: 
      result = b
  else: 
    #one or both numbers are odd
    if a > b:
      result = a
    else: 
      result = b
  return result 

#--clean up using the min function--
def lesser_of_two_evens2(a,b):
  if a%2 == 0 and b%2 == 0: 
    #Both numbers are even
    return min(a,b)
  else: 
    #one or both numbers are odd
    return min(a,b)

# Write a function that takes in a 2-word string and returns Trues if boh words begin with the same letter
def animal_crackers(text): 
  wordlist = text.split()

  first = wordlist[0]
  second = wordlist[1]

  return first[0] == second[0]
#Or use double indexing to condense code
def animal_crackers2(text):
  wordlist = text.lower().split
  return wordlist[0][0] == wordlist[1][0]

#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
  if n1 + n2 == 20:
    return True
  elif n1 == 20: 
    return True
  elif n2 == 20: 
    return True
  else: 
    return False
print(makes_twenty(20,20))
#OR use or
def makes_twenty20(n1,n2): 
  return ((n1+n2) == 20) or (n1 == 20) or (n2 == 20) 
print(makes_twenty20(20,10))

print('\n')
#---LVL 1 FIGHT---
#Capitalize tge first and fourth letters of a name. 
def old_mcdonald(name):
  first = name[0].upper() 
  inbetween = name[1:3]
  fourth = name[3].upper()
  rest = name[4:]
  return first+ inbetween + fourth + rest
print(old_mcdonald('macdonald'))
#OR use the capitalize method
def old_macdonald(name):
  firsthalf = name[:3]
  secondhalf = name[3:]
  return firsthalf.capitalize() + secondhalf.capitalize()
print(old_macdonald('macdonald'))

#Given a sentence, return a sentence with the words reversed. 
#use join to convert list of strings into one list. 
def master_yoda(text): 
  wordlist = text.split()
  reverse_wordlist = wordlist[::-1]
  return ' '.join(reverse_wordlist)
print(master_yoda('I am home'))

#Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n): 
  return (abs(100-n) <= 10) or (abs(200-n) <= 10)
print(almost_there(50))

#---LVL 2 FIGHT---
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
  for i in range(0,len(nums)-1): 
    if nums[i] == 3 and nums[i+1] == 3:
      return True
  return False

#Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
  result = ''
  for char in text:
    result += char * 3 
  return result
  
print(paper_doll('hello'))

#Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum(even after adjustment) exceeds 21, return 'Bust'
def blackjack(a,b,c): 
  bj = sum([a,b,c])
  if bj <= 21: 
    return bj 
  elif 11 in [a,b,c] and bj >= 31:
    return bj - 10
  else:
    return 'BUST'

print(blackjack(5,9,3))

#Return the sum of the numbers in the arrau, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9) Return 0 for no numbers
def summer_69(arr):
  total = 0
  add = True
  for num in arr: 
    while add: 
      if num != 6:
        total += num
        break
      else: 
        add = False
    while not add: 
      if num != 9: 
        break
      else: 
        add = True
        break
  return total


#print(dir())
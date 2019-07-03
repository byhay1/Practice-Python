#----------------
#Lambda, Map and Filter Functions...
#----------------

#-------
#Start with MAP function, maps index to function
#-------

def square(num):
  return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums): 
  print(item)

#or if you want to return the LIST  use...
print(list(map(square,my_nums)))
print('\n')

#String stuff new function
def splicer(mystring):
  if len(mystring)%2 == 0:
    return 'EVEN'
  else: 
    return mystring[0]

names = ['Andy','Michael','Dwight']
print(list(map(splicer,names)))
print('\n')

#-------
#Next, the FILTER function (True or False)
#-------

def checkeven(num): 
  return num % 2 == 0

mynums = [1,2,3,4,5,6]
print(list(filter(checkeven, mynums)))

#-------
#Final, Lambda...
#-------

def square2(num): 
  result = num ** 2
  return result

#-----Lambda time-----#
#used for anonymous functions
lambda num:  num ** 2
####example using lambda with the map function
print(list(map(lambda num: num ** 2, mynums)))
#first LAMBDA function and mynums get chosen as variables
#second MAP function maps each num/index into lambda function
#third each result is cast to a LIST
#fourth, PRINT
####example 2 using filter
print(list(filter(lambda num: num % 2 == 0, mynums)))
#Get first letter from names
print(list(map(lambda letter: letter[0], names )))
#Get the reverse string
print(list(map(lambda string: string[::-1], names)))


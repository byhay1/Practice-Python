#--------
#Lets do for loops
#used to iterate through an object, list, etc. 
# syntax
# my_iterable = [1,2,3]
# for item_name in my_iterable
#     print(item_name)
# KEY WORDS: for, in
#--------

#first for loop example
mylist = [1,2,3,4,5,6,7,8,9,10]

#for then variable, you chose the variable
print('\n')
for num in mylist: 
  print(num)

#or you can print whatever you want, flexible
print('\n')
for num in mylist: 
  print ('Hi')

#ctrl flow with for loops
print('\n')
for num in mylist:
  if num % 2 == 0: 
    print (num, 'even')
  else: 
    print (num, 'odd future')

#get the sum of everything using loop
listsum = 0

print('\n')
for num in mylist: 
  listsum = listsum + num
print(listsum)

#show all by putting it in the for loop through indentation

print('\n')
for num in mylist:
  listsum = listsum + num
  print(listsum)

#do for strings
print('\n')
mystring = 'Hello World'
for letter in mystring:
  print (letter)

#can use the underscore when you are not assigning variables '_'
print('\n')
for _ in mystring: 
  print("don't you dare look at me")

#tuple stuffs, tuple unpacking 
print('\n')
mylist2 = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist2))
#return tuples back using a for loop
for item in mylist2: 
  print(item)
#Or you can do the following
#(a,b) does not need '()'
print('\n', 'unpacking the tuples!')
for (a,b) in mylist2: 
  print(a)
  print(b)

#------------
#iterating through a dictionary
#------------
d = {'k1':1,'k2':2,'k3':3}
#only iterating the Key... not the value
#if you want only the value use .values()
print('\n')
for item in d: 
  print(item)

#------------
#If you want to iterate the value use the .items() 
#This will give you the full item tuple set.
#------------

for item in d.items(): 
  print(item)
#use unpacking to get the dictionary values
for key, value in d.items():
  print(key, '=', value)
 

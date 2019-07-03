#----------
#List comp
#----------

mystring = 'hello'
# the noob way to do it
mylist = []
for letter in mystring: 
  mylist.append(letter)
  print (mylist) # shows each iteration through the list

#better way to list
print('\n')
mylist2 = [letter for letter in mystring]
print(mylist2)

#use to get full scope of list, can use range function.
#basically applying .append without using it by inputing the loop within the list. 
print('\n')
mylist3 = [num for num in range(0,11)]
print(mylist3)

#can even perform operations on the "loop within the list"
#for this we take the square of each num in the range, and add to the mylist4 list.
print('\n')
mylist4 = [num**2 for num in range(0,11)]
print(mylist4)

#get even numbers
#hard way... aka my way... 
print('\n')
mylist5 = [num%2 for num in range(0,11)]
print(mylist5)
for num in mylist5: 
  if num == 0: 
    print('even')
  else: 
    print('odd')

#teacher way if I waited to see how it was done
print('\n')
mylist6 = [num for num in range(0,11) if num%2 == 0]
print(mylist6)

#one more example
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print('\n',fahrenheit)

#break it out in for loop
fahrenheit2 = []
print('\n')
for temp in celcius: 
  fahrenheit2.append((9/5)*temp + 32)
print(fahrenheit2)

#---------
#if/else into a list comprehension
#---------
print('\n')
result = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
print(result)

#---------
#nest loop in list comp
#---------
print('\n')
mylist7 = []
for x in [2,4,6]:
  for y in [100,200,300]:
    mylist7.append(x*y)
    print(mylist7)

#list comp example
mylist8 = [x*y for x in [2,3,4] for y in [1,10,100]]
print('\n',mylist8)




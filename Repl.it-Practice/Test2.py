#---------
#Test Python knowledge of statements
#---------

#---1---
#Use for, .split() and if to create a statement that will print out the words that start with 's': 
st = 'Print only the words that starts with s in this sentence'
onlyS = []

for word in st.split(' '): 
  if word[0] == 's': 
    onlyS.append(word)
print(onlyS)
print('\n')

#---2---
#Use range() to print all the even numbers from 0 to 10
oneten = []
for num in range(0,11,2): 
  oneten.append(num)
print(oneten)
# OR LIST COMP
oneten = [num for num in range(0,11,2)]
print(oneten,'\n')


#---3---
#Use list comprehension to create a list of numbers between 1 and 50 that are divisible by 3
onefifty = [num for num in range(0,51) if num%3 == 0]
print(onefifty)

#---4---
#Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'
st2combine = ''

for word in st2.split(' '):
  if len(word) % 2 == 0:
    print(word,'',)
    st2combine += word + ' '
  else:
    print('')
print(st2combine)
print('\n')

#---5---
#Write a program that prints the integers from 1 to 100. But for multiples of 3 print "Fizz"
#Multiples of 5 print "Buzz"
#Multiples of both 3 and 5 print "FizzBuzz"
numcombine = []

for num in range(1,101): 
  if num % 3 == 0: 
    numcombine.append('Fizz')
    if num % 5 == 0: 
      numcombine[num - 1] = 'FizzBuzz'
    else:
      pass
  elif num % 5 == 0: 
    numcombine.append('Buzz')
    if num % 3 == 0: 
      numcombine[num -1] = 'FizzBuzz'
    else:
      pass
  else: 
    numcombine.append(num)
print(numcombine)
   
#OR

#for num in range(1,101):
#  if num%3 == 0 and num%5 ==0:
#    print('FizzBuzz')
#  elif num%3 == 0: 
#    print('Fizz')
#  elif num%5 == 0:
#    print('Buzz')
#  else: 
#    print(num)
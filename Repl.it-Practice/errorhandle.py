########################
#Error handling
##############
# Three Key Words
### - try:
# This is he block of code to be attempted (may lead to an error)
### - except:
# Block of code wukk execute in case there is an error in try block
### - finally:
# A final block of code to be executed, regardless of an error.
#########################

def add(n1,n2):
  print(n1+n2)

#if you try to add str and int it will not work so you need error handling
#####TRY, EXCEPT, ELSE BLOCK#####
try: 
  # Want to attempt this code
  #May have an error
  result = 10 + 10
except: 
  print("Hey it looks like you aren't adding correctly!")
else: 
  print ("Add went well!")
  print(result)
##########################

try: 
  f = open('testfile','w')
  f.write("Write a test line")
except TypeError:
  print('There was a TypeError')
except OSError: 
  print('Hey you have an OS Error')
finally: 
  print('I always run')

###########################
def ask_for_int():
  while True: 
    try: 
      result = int(input("Please provide a number: "))
    except: 
      print('Whoopsie Daisy, not a number')
      continue
    else: 
      print("Yes, that is a number!")
      break
    finally: 
      print("I will always run at the end!")

ask_for_int()
print('\n')

###########
# Other stuff/HW
###########

#Handle the exception thrown by the code below by using try and except blocks. 


def prob1():
  a,b,c = [1,2,3]
  lit = ['a','b','c']
  for i in lit: 
    try:
      print(i**2)
      continue
    except:
      print("unsupported operand")

prob1()   
print('\n')

#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try: 
  z = x/y
except ZeroDivisionError:
  print("D.Motombo says 'no no no!' ")
finally: 
  print('All Done')

print('\n')

#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs. 

def ask(): 
  while True:
    try: 
      i = int(input("Please enter an integer, NUGGET!: "))
    except: 
      print('An error occured! Please try again!')
      continue
    else:
      break
  
  print("Your num square is: ")
  print(i**2)
  
ask()


  

#-----
#------
#-------
#

x = 25
def printer(): 
  x = 50 
  return x

#####################
#L:Local - Names assigned in any way within a function (def or lambda), and not declared global in that function
#E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
#G: Global(module) - Names assigned at the top-level of a modle file, or declared global in a def within the file
#B: Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError...
#####################

#lambda num:num**2
name = 'THIS IS A GLOBAL STRING'

def greet():
  #ENCLOSING
  name = 'Sammy'

  def hello():
    #LOCAL
    name = 'IM A LOCAL'
    print('Hello ' + name)
  
  hello()

greet()

#-------------

print('\n')
x = 50

def func(x):
  print(f'X is {x}')
  #LOCAL REASSIGNMENT
  x = 200
  print(f'I just locally changed {x}')

print(func(x))

#--------------
#In LOCAL, use GLOBAL to GLOBALLY assign in function
#--------------

print('\n')

def func2():
  global x 
  print(f'X is {x}')
  #LOCAL REASSIGNMENT ON GLOBAL VARIABLE
  x = 200
  print(f'I just globally changed {x}')

func2()
print(x)

#--------------
#return 'x' for cleaner code
#--------------

print('\n')

def func3(x):
  print(f'X is {x}')
  #LOCAL REASSIGNMENT
  x = 200
  print(f'I just locally changed {x}')
  return x

x = func3(x)  
func3(x)


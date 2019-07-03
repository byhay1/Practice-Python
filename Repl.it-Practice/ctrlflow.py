#---------
#Control flow
#using (if , elif, else)
#Makees use of colons and inditations
#example: 
#if some _condition:
  # execute some code
#elif some_other_condition: 
  #execute something
#else: 
  # do something else
#---------

#Example... 
if True: 
  print('It is true')  

#comparison example...
hungry = True
hungry2 = False

# switch variable for different results
if hungry2: 
  print('feed me!')
else: 
  print("I'm not hungry")

#multiple branches using if, elif and else
loc = 'store'

if loc == 'Auto Shop':
  print('cars are cool')
elif loc == 'Bank':
  print('money is fin cool')
elif loc == 'store':
  print('stores are dope')
else:
  print("I do not know much.")

#Another example of if, elif, and else
name = 'Meghan'

if name == 'Frankie': 
  print("Hello Frankie!")
elif name == 'Meghan':
  print('Hello Meghan')
else:
  print('What is your name?')

#don't forget the ':' after each flow statement
#easy to forget.

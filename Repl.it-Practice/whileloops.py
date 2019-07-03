#---------
#while loops
#syntax
#
# while sme_boolean_condition:
#   do something
# else: 
#   #do something different
#---------

#basic while loop
x = 0

while x < 5: 
  print(f'The current value of x is {x}')
  x += 1
else:
  print("X IS NOT LESS THAN 5")

#use break, continue, pass stateents in out loops to add
#additional functionality for various cases. The three
#statements are defined by: 
#-------
#break: breaks out of the current closest enclosing loop.
#continue: Goes to the top of the closest enclosing loop.
#pass: Does nothing at all
#-------

#use pass
x=[1,2,3]

for item in x: 
  # comment
  pass
print('\n end of ghost loop, used as a place holder')

#use continue
mystring = 'Sammy'

for letter in mystring:
  if letter == 'a':
    continue
  print(letter)

#use break
x = 0
while x < 5: 
  if x == 2: 
    break 
  print(x)
  x += 1

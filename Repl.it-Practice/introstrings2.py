#Work on String Properties and Methods

#Immutability, or the ability to NOT change. Strings are immutable
#Only way to change a string is to concatenate
# name[0] = 'P'; will not work

name = "Christine"
last_letters = name[1:]
newName = 'P' + last_letters

#String Concatenation
print('','change the name \n', name, "\n to a name with the first letter 'P' \n", newName, '\n \n')

#Can use other arithmetic to concatenate
print(name * 10, '\n')

#errors occur when you turn a number from int/float to str.
print('',"If you try to add the string 3 + 3 through concatenation you will not get 6. \n", 'Instead you get: ','3'+'3', '\n')

#preventing dynamic assignment
x = 'Hello World'
x.upper() #all upper case
x.lower() #all lower case
x.split() #split a string for a list. Split by white space. If () is defined you can split by definition

#------------------
#Print Formatting with Strings
#------------------

#formatting with the .format method
#put string in location
print('Here we will use the .format method to Insert text. \n',"To use this you use print('<thing>'.format(INSERT))\n",'This is a string {}'.format('INSERTED'))

#.format method, multiple placement
print('The {} {} {}'.format('fox','brown','quick'))

#.format method, multiple placement, use index
print('The {2} {1} {0}'.format('fox','brown','quick'))

#.format with variable assignment
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
print('\n')

#float formatting follows "{value:width.precision f}"
result = 100/133

print('Format through Floats HOMIE \n')

#print regular float
print('Print result from variable: ',result, '\n')
#print string with .format
print('Print using .format method \n',"The result was {r}".format(r = result),'\n')
#print with float formatting
print("Print using float formatting which is {value:width.percision f} \n","The result was {r:1.3f}".format(r = result), '\n')

#------------
#formatting sting literal //new to 3.6
#------------

name2 = "Shely"
name3 = "Red"
age = "29"

print('Hello her name is {}'.format(name2), '\n')
#Or, use the string literal
print('Or you can use a string literal by... \n',"print(f'<thing> {INSERT}')",'\n') 
print(f'Hello, her name is {name2}', '\n')

#Pass multiple variables using string literals
print(f'{name} {name2} {name3} is {age} years old')





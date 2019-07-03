#Variables are dynamic in python. Meaning that one 
#will not need to write the datatype.

a = 5
a = 10
#using the same variable to redefine variable
a = a + a

#if you want to know the type use [type()]
getType = type(a)
print(getType)

#if you assign the type, python changes dynamically
print('lets change the type')
a = 33.3
newType = type(a)
print(newType)

#logic with variables
print('lets try some logic with variables')
my_income = 100
tax_rate = 0.1
tax = my_income * tax_rate
print('I make ', my_income, 'and my tax rat is', tax_rate,'thus I owe...', tax)

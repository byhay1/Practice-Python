#------------
#tuples are immutable and similar to list
#FORMAT of a tuple == (1,2,3)
#------------

# create a tuple similar to a list but use '()' instead of '[]'
#define tuple
t = (1,2,3)
t2 = ('a','a','b')
mylist = [1,2,3]

#want to find the class type use the typle function type(PUTinVAR)
print('',"Find the type of the var 't' by using type(t): ", type(t), '\n', "Find the other type using type(mylist): ", type(mylist),'\n')

#can use other identifiers like a len(PUTinVar) and splice it how you want VAR[start:stop:step]

#find how many times a value occurs in a tuple or list
#do so by using the .count method
print('','There are only two methods you can use to get the count and the index position \n',"So t2.count('a') = ")
print(t2.count('a'))

#get the index num
print("and t2.index('b') = ")
print(t2.index('b'))

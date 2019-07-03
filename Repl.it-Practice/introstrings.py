#use double quotes when you have a single quote in your string
print('Print with a single quote:\n',"I'm going on a run\n")

#escape sequence
print('','Print with an escape:\n','hello \n world\n')

#tab use
print('Print with an tab:\n''hello \t world\n')

#find the length of a string
length = len('I am')
print('Print the length of the string (I am)\n', length,'\n \n \n')

#----------------------------
# String Indexing an String Slicing
#----------------------------
print('______________________________ \n','Now on to string indexing and slicing\n','______________________________')

#string indexing to point to index in array (indexing starts at 0)
mystring = "Hello World"
index0 = mystring[0] #should equal H
index8 = mystring[8] #should equal r
indexNeg2 = mystring[-2] #shoul equal l

print('','Show string for indexing mystring: \n', mystring,"\n when index '0' is called it equals \n", index0,"\n and when index '8' is called it equals \n", index8, '\n')

#negative indexing (negative starts at -1)
print('', "Can also count backwards: \n You can call '-2' and it will equal \n",indexNeg2,'\n')

#Intro to slicing
#Use [start:stop:step] syntax
mystring2 = 'abcdefghijk'
slicestrC = mystring2[2:]
slicestrC2 = mystring2[:3]
slicestrdef = mystring2[3:6]
mystringFull = mystring2[::]

#start from c to the end of the string for slice
print('','Show string for slicing mystring2: \n', mystring2, '\n')
print('',"You can slice by using the index and ':' \n","For this we are going from c to end using 'mystring2[2:]'\n",'If you slice from 2 - END, you get: \n', slicestrC, '\n')

#start from beginning and pick end of string for slice
#index 3 is technically d however, stop means to go up to, BUT NOT INCLUDE, the chosen index
print('',"Slice from beginning to 'c' use 'mystring2[:3]' \n" ,'If you slice from beginning - 3, you get: \n', slicestrC2, '\n')

#slice a part of the string using both start and stops
print('',"Slice from 'd' to 'f' use 'mystring2[3:6]' \n" ,'If you slice from 3 - 6, you get: \n', slicestrdef, '\n')

#call string using [::]
print('','Can print full string by using [::] \n',mystringFull)

#steps are default by 1, but you can us [::step] to iterate by chosen number
print('','steps are default by 1, but you can us [::step] to iterate by chosen number \n','Lets pick [::2] \n', mystring2[::2],'\n OR jump 3 \n', mystring2[::3], '\n')

#reverse string 
print('','How to reverse a string you will use -1 step \n', mystring2[::-1])

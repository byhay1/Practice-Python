#----------
#simple input and output with basic.txt
#(not sure how I am going to do this with repl.it)
#----------


#define where your txt file is
myfile = open('test.txt','r')

#open a txt file by using calling the open function
print('\n',"You can open a text file by using open('test.txt','r') \n","And append .read() so it will be: \n", myfile.read())

#write a sentence using the .write()
x = open('test.txt','w')
x.write('What you talking about Will-I-Am')

#you can close the file using .close()
x.close()
#open again so it can be used
y = open('test.txt','r')

#Then read the file and see what was written.
print('\n', 'Lets see if we can add to the sentence \n', y.read())
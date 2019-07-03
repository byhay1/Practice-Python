#------------
#small introduction to sets
#------------

#define set
myset = set()

#can add to set by using the .add method
myset.add(1)

#when adding to the set it has to be unique or it won't be added
#example add 2 to the set multiple times

myset.add(2)
#should have the set equal {1,2}
#try adding anther and it will be the same no matter how many times the .add() methos is called.

#---
#cast list in a set to get the unique values
#---

#define list
mylist = [1,1,1,2,2,2,2,3,3]

print('', "Cast your list into a set by using set(mylist)  \n which is equal to: ", set(mylist), '\n')
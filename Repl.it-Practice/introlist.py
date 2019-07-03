#----------------------------
#Introduction to list in python
#----------------------------

my_list = [1,2,3]
my_list2 = ['STRING', 100, 23.2]
my_list3 = ['one','two','three']
add_list = ['four','five']
new_list = my_list3 + add_list
new_list2 = ['a','e','x','b','c']
num_list = [4,1,8,3]
num_list2 = [4,1,8,3]

#check length of list using 'len' 
print('',"check the length of the list by using 'len(LIST)' \n", 'For [string, #, #] it should show:',len(my_list2))

#grabbing specific elements within list
print('\n', my_list3[0])

#go from element 2 to 3, skip 1
print('\n', my_list3[1:3])

#concatenate list
print('\n',my_list3 + add_list,'\n')

#--------
#list are mutable, unlike strings. REMEMBER THAT
#--------

#can change an element in a list by reassigning it 
new_list[0] = 'ONE ALL CAPS'
print('We have changed the new_list with 1,2,3,4,5 to:', '\n', new_list, '\n')

#add to list using append method to the end of a list
new_list.append('six')
print('We can also add to a list using the .append() method: \n', new_list, '\n')

#to remove an element, use pop method
new_list.pop()
popped_item = new_list.pop()
print('We can also remove the (six) by using the .pop method: \n', new_list, '\n')
print('Also we can save the .pop() element within a variable: \n',popped_item, '\n')

#can also remove by index position
new_list.pop(0)
print('Can also remove by index position, pass .pop(#) : \n', new_list, '\n')

#can use the sort method to sort stuff in "order"
print("Can sort ['a','e','x','b','c']", 'in order by using .sort() method', new_list2.sort(), new_list2, '\n And .sort() method returns none \n')

print("Can sort [4,1,8,3]", 'in order by using .sort() method', num_list.sort(), num_list, '\n')

#you can reverse the list  using the reverse method
num_list.reverse
print("Can reverse the list [4,1,8,3] by using .reverse() method", num_list2.reverse(), num_list2, '\n')
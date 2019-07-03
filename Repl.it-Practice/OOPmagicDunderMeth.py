#----------
# Introduction to OOP: 
# Magic/Dunder Methods
#
#----------

mylist = [1,2,3]

#build class
class Book: 
  def __init__(self, title, author, pages): 
    self.title = title
    self.author = author
    self.pages = pages
#relate to the str method, using the special method __str__
  def __str__(self):
    return f"{self.title} by {self.author}"
#relate to the len method to get length, using the special method __len__
  def __len__(self):
    return self.pages
#relate to del method to delete items , using __del__
#  def __del__(self):
#    return "A book has been deleted"

b = Book('Python rocks','Jose',200)
print(b)
print('The length of the book is',len(b))

##Deleting stuff from class##
#-----------
#Use the 'del' and then followed by what you want deleted
#-----------
##
# Will delete the book and print "A book has been deleted because of the definition of __del__ within the class"
#del b






#---------
#Test Python knowledge of functions and methods
#---------

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line

class Line: 
  def __init__(self, coor1, coor2):
    self.coor1 = coor1
    self.coor2 = coor2
  def distance(self): 
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    dist = (((x2-x1)**2)+((y2-y1)**2))**.5
    return dist
  def slope(self): 
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    slp = (y2-y1)/(x2-x1)
    return slp

coordinate1 = (3,2)
coordinate2 = (8,10)

lin = Line(coordinate1, coordinate2)

print(lin.distance())
print(lin.slope())
print('\n')

#Create a cylinder class
import math 

class Cylinder: 
  def __init__(self,height=1, radius=1): 
    self.height = height
    self.radius = radius
  def surface_area(self): 
    sa = ((math.pi*self.radius**2)*2) + ((self.radius*2*math.pi)*self.height)
    return sa
  def volume(self): 
    vol = (math.pi*self.radius**2)*self.height
    return vol

c = Cylinder(2,3)

print(c.surface_area())
print(c.volume())
print('\n')

#Challenge Question ---Bank Account Class---
# Create a bank account class that has two attributes 
# - owner
# - balance
# and two methods:
# - deposit 
# - withdraw
#As an added requirement withdrawals may not exceed the available balance
#####
#Instantiate your class, make several deposits and withdrawal, and test to make sure the account can't be overdrawn
#####

class Account: 
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self,dep_amt):
    self.balance = self.balance + dep_amt
    print(f"Added {dep_amt} to the balance")
  
  def withdrawal(self,wd_amt):
    if self.balance >= wd_amt: 
      self.balance = self.balance - wd_amt
      print(f"Withdrew {wd_amt} from the balance")
    else: 
      print("Insuffient Funds")
  
  def __str__(self):
    return f" Owner: {self.owner} \n Balance: {self.balance}"


# 1. Instantate the class
acct1 = Account('Emily',500)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals, should print "deposit accepted" OR "withdrawl accepted"
acct1.deposit(50)

acct1.withdrawal(75)

# 6. Make a withdrawal that exceeds the available balance, should print "Funds Unavailable"
acct1.withdrawal(500)






#one.py

def func():
  print("Func() In one.py")

print("Top Level In one.py")

if __name__ == '__main__':
  print('One.py is being run directly!')
else: 
  print('One.py has been imported')
####################
# A tic-tac-toe game for two people
# Created with <3 Pyron
####################

#create a board
board = [[7,8,9],[4,5,6],[1,2,3]]
#empty boards to place X's and O's in
#user1_X = [[],[],[]]
#user2_O = [[],[],[]]

#Ask Player 1 to be X or O
player1 = str(input('Player 1: Do you want to be X of O? ', ))
#If X, player one will go first
if player1.upper() == 'X': 
  print("Player 1 will go first")
else: 
  print("Player 2 will go first")
print('\n')

#Ask if ready to play
r_u_rdy = str(input('Are you ready to play? Enter Yes or No. '))

def ready(r_u_rdy):
  if r_u_rdy.upper() == 'YES': 
    x = int(input('Please make your selection on the keypad: '))
  elif r_u_rdy.upper() == 'NO':
     print('Want to play?...')
     pass
  else: 
    print('Please type a valid response and try again')
    

while True: 
  if r_u_rdy.upper() != 'YES' or 'NO':
    r_u_rdy = str(input('Yes? or No? '))
    ready(r_u_rdy)


'''
#user input loop
def user_input(int(x)):
  for row in board: 
    for index, num in row.split():
      if x == num[index]:  
        num[index] = 'X'
      else: 
        print("Please select a valid numerical input")
    return num[index]
  return
return 
'''




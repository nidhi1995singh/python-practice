last_atempt=''
def print_board():
	print(' '+board[6]+' | '+board[7]+' | '+board[8])
	print('---------')
	print(' '+board[3]+' | '+board[4]+' | '+board[5])
	print('---------')
	print(' '+board[0]+' | '+board[1]+' | '+board[2])
board=['']*9

def nxt_board():
	print('\n'*1)

print ('Welcome to Tic Tac Toe !')
player1 = input('Player 1 : Do you want to be X or O ? ')
while player1!='x' and player1!='X' and player1!='o' and player1!='O':
	player1= input('PLayer 1 : Do you want to be X or O ? ')

if player1=='x' or player1=='X':
	player1='X'
	player2='O'
else:
	player1='O'
	player2='X'
 	
print ('Player 1 will go first.')

position= input('Enter the position where you want to place your '+player1+' ? ')
board[position-1]=player1
last_atempt=player1

print_board()
while board.count('')>0:
	if last_atempt=='X':
		position= input('Enter the position where you want to place your '+player2+' ? ')
		board[position-1]=player2
		last_atempt=player2
	else:
		position= input('Enter the position where you want to place your '+player1+' ? ')
		board[position-1]=player1
		last_atempt=player1
	print_board()
	nxt_board()
else:
	print ('Match Draw')
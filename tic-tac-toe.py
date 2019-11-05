
def display_board(board):
	print(board[7]+'|'+board[8]+'|'+board[9])
	print('-----')
	print(board[4]+'|'+board[5]+'|'+board[6])
	print('-----')
	print(board[1]+'|'+board[2]+'|'+board[3])

dboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def clear_output():
	print('\n'*2)

# ---------- match output ---------------------
def match_pattern(board,player):
	output = []

	if(board[1] == board[2] == board[3] == 'X' or board[1] == board[2] == board[3] == 'O'):
		# output[0] = '1'
		# output[1] = 'O'
		return player
	else:
		# output[0] = '0'
		return False

	# return output		
# ---------- match output end---------------------

player1 = input("Do you want to be 'X' or 'O'")

if player1 == 'X':
	player2 = 'O'
else:
	player2 = 'X'

print('welcome to tic tac toe game')

print('Player1 will go first')

display_board(dboard)

last_atempt = ''

position = int(input('Enter the position where you want to place your '+player1+' ? '))

dboard[position] = player1
last_atempt = player1
display_board(dboard)

while dboard.count(' ')>0:
	if last_atempt==player1:
		position= int(input('Enter the position where you want to place your '+player2+' ? '))
		dboard[position]=player2
		last_atempt=player2
		result = match_pattern(dboard,player2)
		print(result)
	else:
		position= int(input('Enter the position where you want to place your '+player1+' ? '))
		dboard[position]=player1
		last_atempt=player1
	display_board(dboard)
	clear_output()
else:
	print ('Match Draw')

# if not dboard:
#   print("List is empty")
# else:
# 	display_board(dboard)

# dboard[position] = player1
# display_board(dboard)





#!/usr/bin/python
import random

board = []
def new_board():
	global board
	board = []
	for i in range(5):
		board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)	

#ship_row = random.randrange(5)
#ship_col = random.randrange(5)

#print ship_row, ship_col

def play(turn):
	new_board()
	original_turn = turn
	ship_row = random.randrange(5)
	ship_col = random.randrange(5)
	print_board(board)
	print "Lets play Battleship\
	\nYou have %d chances remaining" %(turn)

	while turn > 0:
		guess_row = raw_input("Guess Ship Row:")
		guess_column = raw_input("Guess Ship Column:")
		if (not guess_row.isdigit()) or (not guess_column.isdigit()):
			print "Please enter a value between 0 to 4"
		else:
			guess_row = int(guess_row)	
			guess_column = int(guess_column)
			if (ship_row == guess_row) and (ship_col == guess_column):
				print "Voila!!! you sanked my ship"
				board[guess_row][guess_column] = "X"
				print_board(board)
				print "Lets play a new game."
				return play(original_turn)
				#break
			elif (guess_row > 4) or (guess_column > 4):
				print "That is not even in the ocean,try again"
				print_board(board)
				print "You have %d chances remaining" %(turn)
			elif board[guess_row][guess_column] == "-":
				print "You already guessed this, try again" 
				print_board(board)	
				print "You have %d chances remaining" %(turn)
			else:
				print "You missed my ship, Try again"
				turn -= 1
				board[guess_row][guess_column] = "-"
				print_board(board)
				print "You have %d chances remaining" %(turn)
				if turn == 0:
					print "My ship was at row %d and colum %d" %(ship_row,ship_col)
					board[ship_row][ship_col] = "X"
					print_board(board)


play(3)


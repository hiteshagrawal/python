#!/usr/bin/python

import random
board = []
size = 0


def board_print():
	global board
	for row in board:
		print " ".join(row)


def new_game():
	global board,size
	board = []
	size = input("Enter board size:") ## Input will automatically convert it to integer
	for row in range(size):
		board.append(["0"] * size )
	board_print()	
	play(3)	


def play(turn):
	global board
	my_ship_row = 	random.randrange(size)
	my_ship_col = 	random.randrange(size)
	print "My ship position is row: %d , column: %d" %(my_ship_row,my_ship_col)
	while turn > 0:
		print "Remaining number of chances: %d"%(turn)	
		guess_row = input("Please enter a row number:")
		guess_col = input("Please enter a col number:")
		if my_ship_row == guess_row and my_ship_col == guess_col:
			print "You busted my ship"
			board[guess_row][guess_col] = "X"
			board_print()
			print "You have WON, starting a new game"
			new_game()
		elif (guess_row + 1 ) > size  or (guess_col + 1) > size:
			print "This is not even in the ocean, try again"
			continue	
		elif board[guess_row][guess_col] != "-" :
			print "My ship is not at this location"
			board[guess_row][guess_col] = "-"
			board_print()
			turn -= 1
		elif board[guess_row][guess_col] == "-" :
			print "You already guess this location, try again"
			board_print()
			continue
	else:
		print "Remaining number of chances: %d"%(turn)
		board[my_ship_row][my_ship_col] = "X"	
		print "My Ship was at location \"X\""
		board_print()
		print "You have lost, starting a new game"
		new_game()
		#board_print()
	
					
new_game()

		


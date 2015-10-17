#!/usr/bin/python
import random
board = []

for i in range(5):
   board.append(["O"] * 5)

#print board   

def board_print(board):
   for row in board:
       print " ".join(row)
   return 

#print board
board_print(board)

## Now hide our ship
my_ship_xaxis = random.randrange(5)
my_ship_yaxis = random.randrange(5)

#print "My ship position is: %d , %d " % (my_ship_xaxis,my_ship_yaxis)

def guess_loc(count):
	count = count
	print "You have %d Guesses" %(count)
	while count != 0:
		try:
			my_xaxis = int(raw_input("Enter X axis for the ship between 0 to 4: "))
			my_yaxis = int(raw_input("Enter Y axis for the ship between 0 to 4: "))
		except:
			print "You entered a wrong value, try again"
			continue	
		if not (my_xaxis in range(5)) or not (my_yaxis in range(5)):
			print "This is not even in the ocean\n Try again:"
			continue
		elif my_xaxis == my_ship_xaxis and my_yaxis == my_ship_yaxis:
			print "You have busted my ship"
			board[my_xaxis][my_yaxis] = "X"
			board_print(board)
			break
		else:
			print "Try another guess:"
			count -= count
			print "Remaining guesses:" + str(count)
			print ""

guess_loc(3)			
		
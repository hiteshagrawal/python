#!/usr/bin/python
import random
board = []

for i in range(5):
   board.append(["O"] * 5)

def board_print(board):
   for row in board:
       print " ".join(row)
   return 

#print board
board_print(board)

## Now hide our ship

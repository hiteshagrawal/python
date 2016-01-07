#!/usr/bin/python
#http://www.prasannatech.net/2012/07/eight-queens-python.html
BOARD_SIZE = 8 
my_board = []
def new_board():
    global my_board
    my_board = []
    for i in range(BOARD_SIZE):
        my_board.append(["O"] * BOARD_SIZE)

def show_board(my_board):
   for row in my_board:
       print " ".join(row)


def under_attack(column, existing_queens):
    # ASSUMES that row = len(existing_queens) + 1
    row = len(existing_queens)+1
    for queen in existing_queens:
        r,c = queen
        if r == row: return True # Check row
        if c == column: return True # Check column
        if (column-c) == (row-r): return True # Check left diagonal
        if (column-c) == -(row-r): return True # Check right diagonal
    return False   

def solve(n):
    global my_board
    new_board()
    if n == 0: return [[]] # No RECURSION if n=0. 
    smaller_solutions = solve(n-1) # RECURSION!!!!!!!!!!!!!!
    solutions = []
    for solution in smaller_solutions:# I moved this around, so it makes more sense
        for column in range(1,BOARD_SIZE+1): # I changed this, so it makes more sense
            # try adding a new queen to row = n, column = column 
            if not under_attack(column , solution): 
                solutions.append(solution + [(n,column)])
    print "No. of available solutions is", len(solutions) , "for queens" , n 
    
    for queens in solutions:
        print "Print queens" , queens
        new_board()
        for r,c in queens:
            print "row" , r-1 , "Col" , c-1
            my_board[r-1][c-1] = "X"
        show_board(my_board)   

    return solutions

                   

if __name__ == "__main__":
    print solve(2)


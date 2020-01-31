#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [Aneri Shah Username: annishah|2000564352]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# Refered from "https://github.com/pjhanwar/N-Queens-with-Obstacles/blob/master/Nqueens.py" to get idea for checking safe rows and columns.
#-----Start-----
#Check in each row whether it is possible to place a friend in that row or not.
def safe_row(board,row,col):
    for c in range (col-1,-1,-1):
        if board[row][c] in "&#@":
            return True
        elif board[row][c]=="F":
            return False
        else:
            continue
#check in each column whether it is possible to place a friend in that column or not.
def safe_col(board,row,col):
    for r in range (row-1,-1,-1):
        if board[r][col] in "&#@":
            return True
        elif board[r][col]=="F":
            return False
        else:
            continue        
#-----End-----

# Get list of successors of given board state
def successors(board,row,col):
    for r in range(0, len(board)):
        for c in range(0,len(board[0])):
            if (r<=row and c<=col):
                continue
            #check for the constraints and place the friend in the place which satisfies the constraints.
            if (safe_row(board,r,c)==False or safe_col(board,r,c)==False):
                continue
            elif (board[r][c] == '.' ):
                return [add_friend(board, r, c)]
            else:
                continue

                                               
    

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

# Solve n-rooks!
def solve(initial_board):
    for i in range(0,len(initial_board)):
        fringe = [initial_board]
        viewed=[]
        while len(fringe) > 0:
            curr_move = fringe.pop()
            if successors(curr_move,0,i)!=None: 
                for s in successors( curr_move,0,i ):
                    if is_goal(s):
                        return(s)
                    if s in viewed:
                        continue
                    else:        
                        fringe.append(s)
                        viewed.append(curr_move)
                        continue

                    
                    
    return False


# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")



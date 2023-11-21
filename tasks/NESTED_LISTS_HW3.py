############## TIC TAC TOE  ##############
def in_grid_or_not(the_grid,grid_size_n,r,c):# r,c are you postion right now
    if( not 0<=r<grid_size_n and not 0<=c<grid_size_n or the_grid[r][c] != ' '):
        print("wrong input fuck you reenter")
        return 0
    return 1

def winner_or_not(the_grid,grid_size_n):
    # i will store avery single move that that player can move in the grid
    #i will assume that you are starting always from 0th row and 0th col and moving right or down or diagonally(from left)
                                                    #or 0th row and last col and moving left=right or down=down or diagonally(from right)

    lst_of_moves = []
    lst_of_moves.extend([(r,0,0,1) for r in range(grid_size_n)])  #start (0,0) and step with one will be right (0,1)
    lst_of_moves.extend([(0,c,1,0) for c in range(grid_size_n)])  #start (0,0) and step with one will be down (1,0)
    lst_of_moves.append((0,0,1,1))  #start (0,0) and step with one will be right diagonal (1,1)
    lst_of_moves.append((0, grid_size_n-1 ,1 ,-1 ))  # start (0,last_col) and step with one will be left diagonal (1,-1)

    for r,c,row_move,col_move in lst_of_moves: # for checking direction starting from row 0 or 1 or 2 and col 0 or 1 or 2
        winner = 1
        player_ = the_grid[r][c]
        if (the_grid[r][c] == ' '):  # you musnt fill all the grid as on the final move O may have some oter steps left
            continue  # there is a lot of postions to chech in right and down and diagonal
        for winning in range(grid_size_n):   # for checking direction in right or down or diagonal
            if(player_ != the_grid[r][c]):
                winner = 0
                break
            r,c = r+row_move , c+col_move

        if (winner): # you musnt complete the grid
            return player_

    return None


player = 'XO'
grid_size_n = int(input("Enter grid size: "))  #grid n*n size
the_grid = [[' ']*grid_size_n  for i in range(grid_size_n)]  #creating the grid col#=row#
                                                             #the rows must be lists #
                                                            #the grid must be 2d grid
                                                              #' ' must be replaced with X or O
turn_of_palyer = 0
flag_of_input=0
while(1):
    if ((winner := winner_or_not(the_grid, grid_size_n)) is not None):
        print(f"the winner is {winner}")
        break
    while(not flag_of_input):     #checking input answer
        print('\n'.join(['|'.join(row) for row in the_grid]))
        r, c = map(int, input(f"enter {player[turn_of_palyer]} your move in two steps: ").split())
        r, c = r - 1, c - 1  # must be zero based input
        flag_of_input = in_grid_or_not(the_grid, grid_size_n,r,c)
        if(flag_of_input == 1 ):
            the_grid[r][c] = player[turn_of_palyer]
            turn_of_palyer = 1- turn_of_palyer
            print('\n'.join(['|'.join(row) for row in the_grid]))
            flag_of_input = 0
            break










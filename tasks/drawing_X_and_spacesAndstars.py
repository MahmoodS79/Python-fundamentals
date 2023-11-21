"""
rows=int(input("enter rows"))
var_row_jumping=1               #counts the row you are in

while(var_row_jumping <= rows):
    count_space=0
    count_star=0
    while(count_space < (rows - var_row_jumping )):
        print(' ',end='')
        count_space += 1
    while (count_star < (2*var_row_jumping - 1)):
        print('*', end='')
        count_star += 1
    print()
    var_row_jumping += 1

var_row_jumping -= 1                #I am i the new line but i want to draw the last line again so var_row_jumping must be same as before
while(var_row_jumping != 0):
    count_space=0
    count_star=0
    while(count_space < (rows - var_row_jumping )):
        print(' ',end='')
        count_space += 1
    while (count_star < (2*var_row_jumping - 1)):
        print('*', end='')
        count_star += 1
    print()
    var_row_jumping -= 1
"""

# there is 7 rows and 7 characters in one row ex: (*     *) == 7 chars
rows=int(input())
for i in range(rows):
    for i_1 in range(rows):
        if(i == i_1 or rows-1-i == i_1  ):
            ''' for drawing the second diagonal and counting the col you are standing at in one row'''
            print("*",end='')
        else:
            print(" ",end='')
    print()


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#solving with backtracing
def solve(ins):
    found = find(ins)
    if not found:
        return True
    else:
        row,column = found

    for i in range(1,10):
        if possible(ins,i,row,column):
            ins[row][column] = i
            print(row,column,i)
            if solve(ins):
                return True
            
            ins[row][column] = 0
    return False

#find empty slots
def find(ins):
    for i in range(len(ins)):
        for j in range(len(ins[0])):
            if ins[i][j] == 0:
                return i , j
    return None


# checking if the chiosen number fits the slot
def possible(ins,num,row,column):
    for i in range(len(ins)):
        if ins[row][i] == num:
            return False


    for j in range(len(ins[0])):
        if ins[j][column] == num:
            return False

    cube_row = int(row//3)
    cube_column = int(column//3)
    for i in range(3*(cube_row),3*(cube_row)+3):
        for j in range(3*cube_column,3*(cube_column)+3):
            if ins[i][j] == num:
                return False

    return True

#displaying the board
def display(ins):
    for i in range(len(ins)):
        if i%3 == 0 and i != 0 :
            print("- - - - - - - - - - - - - - ")
        for j in range(len(ins[i])):
            if j %3 == 0 and j !=0 :
                print("|",end="")
            if j == 8:
                print(ins[i][j])
            else:
                print(ins[i][j]," ",end="")

    return


display(board)
print("")
solve(board)
print("")
display(board)
"""
---------------GLOBAL PROPS------------------
"""
rank= None
is_win= False
counter= 0

x_array=[]
o_array=[]
matrix=[]


"""
---------------FUNCTIONS----------------------
"""
def build_matrix():
    global matrix
    global x_array
    global o_array

    for row in range(0,rank):
        matrix.append([])
        for col in range(0,rank):
            matrix[row].append(row*rank+col+1)

    for element in range(0,rank*2+2):
        x_array.append(0)
        o_array.append(0)


def get_position():
    global rank
    global matrix
    global counter

    for row in range(0,rank):  
        strFormat=""  
        for col in range(0,rank):
            strFormat+=str(matrix[row][col]) + " | "
        print(strFormat)
        print("-----------")

    if counter%2==0:
        char="x"
    else:
        char="o"

    print("************ user ",char,"****************")
    return int(input("Enter the position (1 - "+ str(rank*rank)+")"))


def check_if_win(row,col):
    global counter
    global is_win
    global rank
    global x_array
    global o_array

    if counter%2==0:
        arr=x_array
    else:
        arr=o_array

    arr[row]+=1
    arr[rank+col]+=1

    if row==col:
        arr[rank+rank]+=1

    if (row+col)==(rank-1):
        arr[rank+rank+1]+=1


    is_win=(arr[row]==rank) or (arr[rank+col]==rank) or (arr[rank+rank+1]==rank) or (arr[rank+rank]==rank)

    if(is_win):
        if(counter%2==0):
            print("x won")
        else:
            print("o won")
    else:
        if(counter==(rank*rank)):
            is_win=True
            print("Game Over")




def handle_turn(position):
    global matrix
    global counter
    row=(position-1)//rank
    col= (position-1) %rank

    if matrix[row][col]!="x" and matrix[row][col]!="o":
        if counter%2==0:
            matrix[row][col]="x"
        else:
            matrix[row][col]="o"

        check_if_win(row,col)

        # change the turn to the other player
        counter+=1
        return True

    else:
        return False



"""
---------------MAIN CODE-----------------------
"""

rank=int(input("Enter the rank of the board: "))
build_matrix()

while not is_win:
    valid_input=False
    while not valid_input:
        selectedPos=get_position()
        valid_input=handle_turn(selectedPos)













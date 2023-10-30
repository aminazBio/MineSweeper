import random

#to increase the limit for running the game to the last possible one here: "50*50 table!"
import sys
sys.setrecursionlimit(10**9)

def create_board(board_size,num_mines):
    
    #global variables which we need in some other functions
    global size,board,Board,mines

    size=board_size
    board={}
    #Board is a copy of the main board which used to decrease recursions in the revealing part
    Board={}
    mines=[]
    
    #boards making
    for A in range(size):
        for B in range(size):
            board[(A,B)]="#"
            Board[(A,B)]="#"

    #mines are placing in their random positions
    trash=[]
    for m in range(num_mines):
        while True:
           i=random.randrange(size)
           j=random.randrange(size)
           if (i,j) not in trash:
               mines.append((i,j))
               trash.append((i,j))
               break

def print_board():
    
    #here we have some additional parts for numbering rows and columns which will help user to determine their goal postion on table
    #in these numberings, we have two different parts: one is before number 10 which because of availability of one digit we havent any problem, but the other one is numbers which are higher than 10 with two digits which was making problems for spacings and I solved them according to my code below there:   
    t=[]
    p=[]
    h=0
    for z in range(1,size+1):
        h+=1
        if h<=10:
            t.append(str(z))
        elif h>10:
            p.append(str(z))
    
    if size<=10:
        T="    "+" ".join(t)
        print(T)
    elif size>10:
        T="    "+"  ".join(t)
        P=" ".join(p)
        print(T+" "+P)  
    
    print()

    l=list(board.values())
    f=[]
    n=0
    c=1
    d=0
    for x in range(size):
        d+=1
        for y in range(size):
            f.append(l[n])
            n+=1

        if size<=10:
            s=" ".join(f)
        elif size>10:
            s="  ".join(f)       
        

        if d<10:
            print(str(c)+"   "+s)
        elif d>9:
            print(str(c)+"  "+s)
        
        c+=1
        f=[]
       
def put_flag(row,col):
    board[(row,col)]="p"
    
def remove_flag(row,col):
    board[(row,col)]="#"

def count_mines(row,col):
    count=0
    if (row-1,col+1) in mines:
        count+=1
    if (row-1,col) in mines:
        count+=1 
    if (row-1,col-1) in mines:
        count+=1
    if (row,col+1) in mines:
        count+=1
    if (row,col-1) in mines:
        count+=1
    if (row+1,col+1) in mines:
        count+=1
    if (row+1,col) in mines:
        count+=1
    if (row+1,col-1) in mines:
        count+=1

    return count

def reveal_cell(row,col):
    if (row,col) in mines:
        board[(row,col)]="@"
        for (row,col) in mines:
            board[(row,col)]="@"
    else:
        board[(row,col)]=str(count_mines(row,col))
        del Board[(row,col)]

        #to reveal other neighbor empty cells after revealing an empty one at first
        if str(count_mines(row,col))=="0":
            if (row-1,col-1) in Board:
                reveal_cell(row-1,col-1)
            if (row-1,col) in Board:
                reveal_cell(row-1,col)
            if (row-1,col+1) in Board:
                reveal_cell(row-1,col+1)
            if (row,col-1) in Board:
                reveal_cell(row,col-1)
            if (row,col+1) in Board:
                reveal_cell(row,col+1)
            if (row+1,col-1) in Board:
                reveal_cell(row+1,col-1)
            if (row+1,col) in Board:
                reveal_cell(row+1,col)
            if (row+1,col+1) in Board:
                reveal_cell(row+1,col+1)
        
def won(num_mines):
    count=0
    for a in range(size):
        for b in range(size):
            if board[(a,b)] == "p":
                if (a,b) in mines:
                    count+=1
    
    #if we want all cells to be revealed before winning
    '''
    cell=0
    for a in range(size):
        for b in range(size):
            if board[(a,b)] != "#" and board[(a,b)] != "p":
                cell+=1
    '''

    if count==num_mines:
        #if cell==((size*size)-num_mines):
            return True   
    else:
        return False    

def main():

    board_size=int(input("enter a number for pretending the number of rows and columns:"))

    while board_size==0 or board_size==1:
        print("board size is invalid!")
        board_size=int(input("please enter a valid number for pretending the number of rows and columns:"))

    num_mines=int(input("enter the number of mines:"))
    
    #to cover and debug some wrong inputs from the user
    while num_mines==0 or num_mines>=(board_size*board_size):
        if num_mines==0:
            print("this game needs at least one mine!")
            num_mines=int(input("please enter valid number of mines:"))
        elif num_mines>(board_size*board_size):
            print("mines are more than the available cells!")
            num_mines=int(input("please enter valid number of mines:"))
        elif num_mines==(board_size*board_size):
            print("mines are equal to the available cells!")
            num_mines=int(input("please enter valid number of mines:")) 

    create_board(board_size,num_mines)

    while reveal_cell != "@":
        s=input("enter your command:")
        if s=="x":
            return "exit"
        S=s.split()
        row=int(S[1])-1
        col=int(S[2])-1
        
        if row not in range(size) or col not in range(size):
            print("Invalid Command!")
        else: 
            if S[0]=="r":
                reveal_cell(row,col)
                print_board()
            elif S[0]=="f":
                put_flag(row,col)
                print_board()
            elif S[0]=="u":
                remove_flag(row,col)
                print_board()    
            else:
                print("Invalid Command!")     
            
            if board[(row,col)]=="@":
                print()
                return "    you lost!"
            if won(num_mines) is True:
                print()
                return "    you won!"    
print(main()) 


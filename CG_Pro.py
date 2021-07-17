import turtle
def fun1(board,y):
    y=y//2
    board.left(120)
    board.forward(y) 
    board.left(60)
    board.forward(y) 
    board.left(120)
    y=y//2
    board.forward(y) 
    board.right(120)
    board.forward(y)
    board.left(120)
    board.forward(y)
    board.left(120)
    board.forward(y)
    board.right(120)
    board.forward(y)
    board.left(120)
    board.forward(y)
    board.right(120)
    board.forward(y)
    board.left(120)
    board.forward(y)
    board.left(120)
    board.forward(y)
    board.right(120)
    board.forward(y)
    board.left(60)
    board.forward(y)
    board.left(120)
    board.forward(y)
    board.right(120)
    board.forward(y)
    board.right(120)
    board.forward(y)
    return (board,y)

def fun2(board,y):
    board.left(120)
    board.left(180)
    z=y
    y=100*x
    board.forward(y//4-z)
    board.right(120)
    board.right(180)
    board.forward(y//4)
    y=y//4
    return (board,y)

def fun3(board,y):
    board.left(120)
    board.forward(y)
    board.right(120)
    y=100*x
    y=y//4
    return (board,y)

def fun4(board,y):
    board.left(120)
    board.forward(y)
    y=100*x
    board.left(120)
    board.forward(y//2)
    y=y//4
    board.left(120)
    board.forward(y)
    return (board,y)

board = turtle.Turtle()
x=4
y=100*x
board.forward(y)
 
board.left(120)
board.forward(y)
 
board.left(120)
board.forward(y)
board,y=fun1(board,y)
#------------------------------------------
board,y=fun1(board,y)
#---------------------
board,y=fun4(board,y)
board,y=fun1(board,y)
#------------------------
board,y=fun4(board,y)
board,y=fun1(board,y)
#------------------------
board,y=fun4(board,y)
board,y=fun1(board,y)
#----------------------
board,y=fun2(board,y)
board,y=fun1(board,y)
#------------------------------
board,y=fun2(board,y)
board,y=fun1(board,y)
#-------------------
board,y=fun2(board,y)
board,y=fun1(board,y)
#---------------------
board,y=fun3(board,y)
board,y=fun1(board,y)
#---------------------
board,y=fun3(board,y)
board,y=fun1(board,y)


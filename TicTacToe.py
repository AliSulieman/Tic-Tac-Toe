board = [[1,2,3],[4,5,6],[7,8,9]]
def my_board(board):
    for row in board:
        values = ""
        for column in row:
            values= values + str(column)+"|"
        print(values)
        print("_"*5)
def player():
    print("pick X or O ")
    Player_one = input().upper()
    player_Two = None
    if Player_one =="X":
        player_Two = "O"
    else:
        player_Two = "X"
    print("Player one is "+Player_one)  
    print("player two is "+player_Two)  
    inProgress = True
    print("Start Playing")
    while inProgress == True:
        my_board(board)
        
        choice  = int(input())
        if choice == 1:
            board[0][0] = Player_one
        if choice == 2:
            board[0][1] = Player_one

          
player()
def display_board(board):
    print(board[1] +"|"+ board[2] +"|"+ board[3])
    print("-----")
    print(board[4] +"|"+board[5] +"|"+ board[6])
    print("-----")
    print(board[7] +"|"+board[8] +"|"+ board[9])
    
def player_input():
    
    marker = " "
    while marker != 'X' and marker != 'O':
        marker = input("Player  Do you want to be X or O?").upper()

        if marker == 'X':
            return('X','O')
        else:
            return('O','X') 

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1]==board[2]==board[3] == mark) or (board[4]==board[5]==board[6] == mark) or (board[7]==board[8]==board[9] == mark) or
    (board[1]==board[4]==board[7] == mark) or (board[2]==board[5]==board[8] == mark) or (board[3]==board[6]==board[9] == mark) or
    (board[1]==board[5]==board[9] == mark) or (board[3]==board[5]==board[7] == mark))

import random

def choose_first():
    choice = random.randint(0,1)
    if choice ==0:
        return 'Player 1'
    else:
        return 'Player 2'    

def space_check(board, position):
    
    return board[position] == " "

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 

def player_choice(board):
    
    position = 0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board,position):
        position = int(input("Enter your  position  inbetween (1-9)"))
    return position

def replay():
    
    choice = input("Do you want to Play again : Enter 'Yes' or 'No' ")
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')

while True:
    test_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    Player1_marker,Player2_marker = player_input()

    turn = choose_first()
    print(turn + " Will play first ")

    play_game = input("Do you want to Play y or n")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False    

#Player 1 Turn.
    while game_on:
        if turn == 'Player 1':
         display_board(test_board)
         position = player_choice(test_board)
         place_marker(test_board,Player1_marker,position)

         if win_check(test_board,Player1_marker):
            display_board(test_board)
            print("Congrats Player 1 has Won")
            game_on = False

         else:

            if full_board_check(test_board):

                display_board(test_board)
                print("It's a Tie Game")
                game_on= False 
            else:
                turn = 'Player 2'   
# Player2's turn.
        else:
            if turn == 'Player 2':
             display_board(test_board)
             position=player_choice(test_board)
             place_marker(test_board,Player2_marker,position)

             if win_check(test_board,Player2_marker):

                display_board(test_board)
                print("Congrats Player 2 has Won")
                game_on = False

             else:

                 if full_board_check(test_board):
                   display_board(test_board)
                   print("It's a Tie Game")
                   game_on= False 
                 else:
                   turn = 'Player 1'      
        
    if not replay():
        break    

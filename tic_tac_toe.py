import random
from IPython.display import clear_output

marker = ' '
test_board = ['#','X','O','X',
            'O','O','O',
            'X','O','X']

def choose():
    player_number=random.randint(0,1)
    if player_number == 0:
        return 'player 1'
    elif player_number == 1:
        return 'player 2'

def player_input(marker=None):

    while marker not in ['X','O']:
      marker = input("enter O OR X :")
      if marker == 'O':
             print("player 1 has choosen O")
             return ('O','X')

      elif marker == 'X':
             print("player 1 has choosen X ")
             return ('X', 'O')
      else:
          print("enter valid choice")


def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
   return(
    #ROW
    (board[1]== board[2] == board[3]== mark) or
    (board[4] ==board[5] == board[6] == mark) or
    (board[7] ==  board[8] ==  board[9] == mark)or
   #COLUMN
    (board[1] == board[4] == board[7] == mark)or
    (board[2] == board[5] == board[8] == mark)or
    (board[3] == board[6] == board[9] == mark) or
   #DIAGONAL
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

def space_check(board,position):
   return board[position]== ' '

def board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    position =0
    # TO ENSURE WE PUT MARKERS IN EMPTY PLACES ONLY
    while position not in [1,2,3,4,5,6,7,8,9] or not  space_check(board,position) :
        position=int(input("choose position from(1-9)"))
    return position

#start code

print("welcome to tic tac toe")

while (1):
    play_game = input('start game Y or N:')
    if play_game == 'Y':
        game = True
    else:
        game = False
        print("bye bye")
        break
    # display empty board
    the_board=[' ']*10
    player_1, player_2 = player_input()
    turn = choose()
    print(turn+' will go first ')

    #game logic
    while game :
        #PLAYER 1
     if turn == 'player 1':
        display_board(the_board)
        position = player_choice(the_board)
        place_marker(the_board,player_1,position)
        #to check if player won
        if win_check(the_board,player_1):
            display_board(the_board)
            print('player 1 won')
            game=False


        else:

          if board_check(the_board):
            display_board(the_board)
            print('tie')
            game=False

          else:
              turn = 'player 2'
# PLAYER 2
     if turn == 'player 2':
         display_board(the_board)
         position= player_choice(the_board)
         place_marker(the_board,player_2,position)

         if win_check(the_board,player_2):
             display_board(the_board)
             print('player 2 wins')
             game=False

         else:
             if board_check(the_board):
                display_board(the_board)
                print('tie')
                game=False

             else:
                 turn= 'player 1'


















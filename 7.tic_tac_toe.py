EMPTY_SLOT = "-"
X_PLAYER = "X"
O_PLAYER = "0"
TIE = "tie"

WIN_COMBINATION_INDICES = [
  # Complete row
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Complete column
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Complete diagonal
  [0, 4, 8],
  [2, 4, 6]
]


def initialize_board():
  board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
  return board


def display_board(board):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


def handle_turn(player, board):
  print(f"{player}, it's your turn.")
  position = input('Please enter a number between 1 and 9: ')
  position = int(position)-1
  
  
  while not valid_position(position,board):
    position = input('Please enter a number between 1 and 9: ')
    position = int(position)-1

  board[position] = player
  display_board(board)

  # TODO Ask player to input a position (1-9). Ask while the position is not valid (check using valid_position)

  # TODO Write player's sign in board

  return board


def valid_position(position, board):
  valid = False
  if position < 0 or position > 8:
    print('Please enter a number between 1 and 9 :')
    valid = False
  elif board[position] != "-":
    print('This position not avaible, enter other location: ')
    valid = False
  else:
    valid = True

  return valid
  


def switch_player(player):
  if player == X_PLAYER:
    player = O_PLAYER
  # Or if the current player was O, make it X
  elif player == O_PLAYER:
    player = X_PLAYER
  # TODO Switch the player: X --> 0 or 0 --> X
  return player


def check_for_winner(board,player):
  winner = None
  filled_slots = 0
  for i in board:
    if i!= EMPTY_SLOT:
      filled_slots+=1


    for item in WIN_COMBINATION_INDICES:
      r1 = item[0]
      r2 = item[1]
      r3 = item[2]
      if board[r1]==player and board[r2]==player and board[r3]==player:
          winner = player
          break
      
  if filled_slots==9 and winner==None:
    winner = TIE

  return winner


def tic_tac_toe():
  winner = None
  game_still_going = True
  player = X_PLAYER  # X will start. TODO (optional): select who starts randomly --> do this in a separate function

  # Initialize board
  board = initialize_board()

  # TODO run this while the game is still going
      # Display board
  

      # Ask the player for a valid position and write it on the board
  while game_still_going:

    display_board(board)

    board = handle_turn(player, board)

    # Check if there is a winner already
    winner = check_for_winner(board,player)
    if winner == player:
      # display_board(board)
      print(f"Congratulations {winner}!!")
      game_still_going = False
    elif winner == TIE:
      # display_board(board)
      print("Tie")
      game_still_going = False
       
        
    
    player = switch_player(player)


  print('The END')


      # TODO stop the game if there is a winner, otherwise switch the player



# Start game
tic_tac_toe()

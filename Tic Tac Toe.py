#TIC TAC TOE GAME Using PYTHON 
def getInput(prompt, cast=None, condition=None, errorMessage=None):
  while True:
      try:
          val = cast(input(prompt))
          assert condition is None or condition(val)
          return val
      except:
          print(errorMessage or "Invalid input.")
def printBoard(board):
  print()
  for row in board:
      print(*row)
  print()
def checkWin(board):
  for row in range(len(board)):
      for col in range(len(board)-1):
          if board[row][col] == "_" or board[row][col+1] == "_" or board[row][col] != board[row][col+1]:
              break
      else:
          return True
  for col in range(len(board)):
      for row in range(len(board)-1):
          if board[row][col] == "_" or board[row+1][col] == "_" or board[row][col] != board[row+1][col]:
              break
      else:
          return True
  for cell in range(len(board)-1):
      if board[cell][cell] == "_" or board[cell+1][cell+1] == "_" or board[cell][cell] != board[cell+1][cell+1]:
          break
  else:
      return True
  for cell in range(len(board)-1):
      emptyCell = board[cell][len(board)-cell-1] == "_" or board[cell+1][len(board)-cell-2] == "_"
      different = board[cell][len(board)-cell-1] != board[cell+1][len(board)-cell-2]
      if emptyCell or different:
          break
  else:
      return True
  return False
def play():
  print("\nN-DIMENSIONAL TIC TAC TOE game.com \n")
  N = getInput(prompt="Enter N, the dimensions of the board: ",
               cast=int,
               condition=lambda x: x >= 3,
               errorMessage="Invalid input. Please enter an integer greater than or equal to 3 as explained")
  board = [['_'] * N for _ in range(N)]
  used = 0
  turn = 0
  while True:
      printBoard(board)
      pick = getInput(prompt=f"Player {turn+1} - Pick location (row, col): ",
                      cast=lambda line: tuple(map(int, line.split(" "))),
                      condition=lambda pair: min(pair) >= 0 and max(pair) < N and board[pair[0]][pair[1]] == "_",
                      errorMessage="Invalid input. Please enter a valid, unoccupied location as an integer pair.")
      board[pick[0]][pick[1]] = "X" if turn == 0 else "O"
      used += 1
      if checkWin(board):
          printBoard(board)
          print(f"Game over, Player {turn+1} wins.")
          break
      elif used == N*N:
          printBoard(board)
          print("Game over. Players have tied the match.")
          print("tic tac toe game ")
          break
      turn = (turn+1)%2
  playAgain = getInput(prompt="Play tic tac toe_Game again? (y/n): ",
                       cast=str,
                       condition=lambda ans: ans.strip("\n").lower() in {"y", "n"},
                       errorMessage="Invalid input. Please enter 'y' or 'n'.")
  if playAgain == 'n':
      print("\nTicTacToe game ended.")
      return
  else:
      play()
if __name__ == '__main__':
  play()
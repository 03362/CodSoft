# Tic-Tac-Toe Board
board = [' ' for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_full(board):
    return ' ' not in board

# Function to check if the game is over
def game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
        if board[i*3] == board[i*3+1] == board[i*3+2] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    # Check for a draw
    if is_full(board):
        return True
    return False

# Function to evaluate the board for the minimax algorithm
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return 1 if board[i] == 'X' else -1 if board[i] == 'O' else 0
        if board[i*3] == board[i*3+1] == board[i*3+2]:
            return 1 if board[i*3] == 'X' else -1 if board[i*3] == 'O' else 0
    if board[0] == board[4] == board[8]:
        return 1 if board[0] == 'X' else -1 if board[0] == 'O' else 0
    if board[2] == board[4] == board[6]:
        return 1 if board[2] == 'X' else -1 if board[2] == 'O' else 0
    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if game_over(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Function to make the AI's move
def make_ai_move(board):
    best_move = -1
    best_eval = -float('inf')
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_eval = minimax(board, 0, False)
            board[i] = ' '
            
            if move_eval > best_eval:
                best_eval = move_eval
                best_move = i
    
    board[best_move] = 'X'

# Main game loop
while not game_over(board):
    print_board()
    player_move = int(input("Enter your move (0-8): "))
    
    if board[player_move] != ' ':
        print("Invalid move. Try again.")
        continue
    
    board[player_move] = 'O'
    
    if game_over(board):
        break
    
    make_ai_move(board)

print_board()

if evaluate(board) == 1:
    print("You win!")
elif evaluate(board) == -1:
    print("AI wins!")
else:
    print("It's a draw!")

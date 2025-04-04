def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_move(board):
    while True:
        try:
            position = int(input("Enter your move (1-9): "))
            if 1 <= position <= 9:
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("That position is already occupied!")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9\n")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row, col = get_valid_move(board)
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()

def print_board(board):
    """Print the game board in a nice format."""
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def check_winner(board):
    """Check if there's a winner. Returns the winner (X or O) or None."""
    # Check rows, columns and diagonals
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    """Check if the board is full."""
    return " " not in board

def main():
    # Initialize the board
    board = [" " for _ in range(9)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom.")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()
    
    while True:
        print_board(board)
        
        # Get player move
        while True:
            try:
                position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
                if 0 <= position <= 8 and board[position] == " ":
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9!")
        
        # Make move
        board[position] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        main()
        if input("Play again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")

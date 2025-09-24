board = [' ' for _ in range(9)]

def print_board():
    print("\n   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   \n")


def check_win(player):

    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def play_game():
    current_player = 'X' 
    print("Welcome to Tic Tac Toe!")
    print("Enter numbers 1-9 to place your mark (1 is top-left, 9 is bottom-right).")
    print_board()

    while True:
       
        try:
            position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid position! Choose 1-9.")
                continue
            if board[position] != ' ':
                print("Position already taken! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue

        board[position] = current_player
        print_board()

        if check_win(current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw():
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()

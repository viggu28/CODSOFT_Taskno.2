def print_board(board):
    for row in board:
        print(' '.join(row))

def empty_indices(board):
    return [i for i, spot in enumerate(board) if spot != "X" and spot != "O"]

def winning(board, player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)   ]        
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
              return True
    return False

def minimax(board, depth, is_maximizing_player):
    if winning(board, "X"):
          return 10 - depth
    elif winning(board, "O"):
          return depth - 10
    elif len(empty_indices(board)) == 0:
          return 0

    if is_maximizing_player:
        best_val = float("-inf")
        for move in empty_indices(board):
            new_board = board.copy()
            new_board[move] = "X"
            val = minimax(new_board, depth + 1, False)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = float("inf")
        for move in empty_indices(board):
            new_board = board.copy()
            new_board[move] = "O"
            val = minimax(new_board, depth + 1, True)
            best_val = min(best_val, val)
        return best_val

def find_best_move(board):
    best_score = float("-inf")
    best_move = None
    for move in empty_indices(board):
        new_board = board.copy()
        new_board[move] = "X"
        score = minimax(new_board, 0, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    board = [" "] * 9
    print(" Tic-Tac-Toe")
    print_board(board)

    while True:
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] != " ":
            print("Invalid move. Try again.")
            continue
        board[player_move] = "O"
        print_board(board)

        if winning(board, "O"):
            print("Congratulations! You win!")
            break

        ai_move = find_best_move(board)
        board[ai_move] = "X"
        print(f"AI's move: {ai_move}")
        print_board(board)

        if winning(board, "X"):
            print("AI wins! Better luck next time.")
            break

        if len(empty_indices(board)) == 0:
            print("It's a draw! Well played.")
            break

if __name__ == "__main__":
    main()

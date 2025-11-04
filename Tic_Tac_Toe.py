from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("❌ Invalid input. Please enter a number between 1 and 9.")
            continue

        move = int(move)
        if move < 1 or move > 9:
            print("❌ Number out of range. Choose between 1 and 9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if str(board[row][col]).isdigit():
            board[row][col] = 'O'
            break
        else:
            print("❌ That spot is already taken. Try again.")


def make_list_of_free_fields(board):
    free = []
    for r in range(3):
        for c in range(3):
            if str(board[r][c]).isdigit():
                free.append((r, c))
    return free


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free = make_list_of_free_fields(board)
    if not free:
        return
    row, col = free[randrange(len(free))]
    board[row][col] = 'X'


board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

while True:
    display_board(board)

    if victory_for(board, 'X'):
        print("💻 Computer wins!")
        break
    elif victory_for(board, 'O'):
        print("🎉 You won!")
        break

    if not make_list_of_free_fields(board):
        print("🤝 It's a tie!")
        break

    enter_move(board)

    if victory_for(board, 'O'):
        display_board(board)
        print("🎉 You won!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("🤝 It's a tie!")
        break

    draw_move(board)
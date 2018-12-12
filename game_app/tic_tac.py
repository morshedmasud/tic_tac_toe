human = "X"
computer = "O"
term = 0
BEST_SPOTS = (4, 0, 2, 6, 8, 1, 3, 5, 7)

# Reset board
def reset(board):
    for i in range(0, 9):
        board[i] = ' '

# Available valid spot
def valid_spot(board):
    av = []
    for i in range(len(board)):
        if board[i] != human and board[i] != computer:
            av.append(i)
    return av


# Check valid or legal spot
def legal_spot(spot, board):
    if board[spot] != human and board[spot] != computer:
        return True
    else:
        return False


# Check possible line base with spot index
def check_posible_line(char, spot1, spot2, spot3, board):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

# CHeck every possible spot throug check_possible_line() function
def check_wins_line(char, board):
    if check_posible_line(char, 0, 1, 2, board):
        return True
    if check_posible_line(char, 3, 4, 5, board):
        return True
    if check_posible_line(char, 6, 7, 8, board):
        return True
    if check_posible_line(char, 0, 3, 6, board):
        return True
    if check_posible_line(char, 1, 4, 7, board):
        return True
    if check_posible_line(char, 2, 5, 8, board):
        return True
    if check_posible_line(char, 0, 4, 8, board):
        return True
    if check_posible_line(char, 2, 4, 6, board):
        return True


# Computer Mover
def computer_move(board):
    # If computer can win,, take this spot
    for spot in valid_spot(board):
        before_assign_value = board[spot]
        board[spot] = computer

        if check_wins_line(computer, board):
            board[spot] = before_assign_value
            return spot
        # undo value of spot
        board[spot] = before_assign_value

    # If human can win,, take this spot
    for spot in valid_spot(board):
        before_assign_value = board[spot]
        board[spot] = human
        if check_wins_line(human, board):
            board[spot] = before_assign_value
            return spot
        # undo value of spot
        board[spot] = before_assign_value

    # If no one can win,, take the best spot
    for spot in BEST_SPOTS:
        if spot in valid_spot(board):
            return spot

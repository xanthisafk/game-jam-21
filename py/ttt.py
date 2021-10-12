# Tic tac toe
import random, time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn = ''
player = ''

def render():
    """
    Displays the current game board.
    """
    global board
    s = f"""{board[0]}|{board[1]}|{board[2]}
-+-+-
{board[3]}|{board[4]}|{board[5]}
-+-+-
{board[6]}|{board[7]}|{board[8]}\n"""

    print(s)

def player_letter():
    """
    Player picks their letter. Also decides who goes first.
    """
    letter = ''

    while letter not in ['x','X','o','O']:
        letter = input('Chose "X" or "O": ')
    
    if random.randint(1,2) == 1:
        first = 'p'
    else:
        first = 'c'

    if letter in ['x','X']:
        return ['X','O',first]
    else:
        return ['O','X',first]

def free_or_not(board,move):
    return board[move] == ' '

def player_move():
    """
    Player's turn.
    """
    global board
    move = ' '

    while move not in [0,1,2,3,4,5,6,7,8] or not free_or_not(board,move):
        move = (int(input("Your turn (1-9): "))-1)
        if move in [0,1,2,3,4,5,6,7,8,9] and free_or_not(board,move):
            break

    return move

def com_move():
    global board

    while True:
        move = random.randint(0,8)
        if board[move] not in ['X','O']:
            return move

def check_full():
    global board
    for i in range(0, 9):
        if free_or_not(board, i):
            return False
    return True

def won(board, letter):
    win = (
        (board[0] == letter and board[1] == letter and board[2] == letter) or # 123
        (board[3] == letter and board[4] == letter and board[5] == letter) or # 456
        (board[6] == letter and board[7] == letter and board[8] == letter) or # 789
        (board[0] == letter and board[2] == letter and board[5] == letter) or # 147
        (board[1] == letter and board[4] == letter and board[7] == letter) or # 258
        (board[2] == letter and board[5] == letter and board[8] == letter) or # 369
        (board[0] == letter and board[4] == letter and board[8] == letter) or # 159
        (board[2] == letter and board[4] == letter and board[6] == letter)    # 357
    )

    return win

def update_board(place):
    global turn
    global board
    board[place] = turn

def switch_player():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

def gameloop():
    global board
    global turn
    global player

    print("Welcome to tic-tac-toe!")
    who = player_letter()
    render()
    
    print("Coin flips...")
    time.sleep(3)

    if who[2] == 'p':
        print("And you go first!")
        p, c = who[0], who[1]
        turn = p
        place = player_move()
    else:
        print("And computer goes first!")
        p, c = who[0], who[1]
        turn = c
        place = com_move()

    update_board(place)
    switch_player()
    render()

    while True:
        if turn == 'X':
            if p == 'X':
                place = player_move()
            else:
                print("Computer's Move:")
                place = com_move()
        else:
            if p == 'O':
                place = player_move()
            else:
                print("Computer's Move: ")
                place = com_move()
        
        update_board(place)
        switch_player()
        render()
        if won(board, turn):
            if who[0] == turn:
                print("You win!")
                break
            else:
                print("You lose. Computer wins.")
                break
        
        if check_full():
            print("Game tied!")
            break

def reset():
    global board, turn, player
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    turn = ''
    player = ''

if __name__ == '__main__':
    gameloop()
    while True:
        q = input("Do you want to play again? (y/n): ")
        q = q.lower()
        if q not in ['y','yes']:
            break
        else:
            reset()
            gameloop()


from random import randint

"""
Board for holding ship locations
"""
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
"""
Board for displaying hits and misses
"""
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
"""
computer create 5 ships
"""


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    while True:
        try:
            row = int(input("Enter the row of the ship: "))
            while row not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print('Not an appropriate choice, please select a valid row')
                row = int(input("Enter the row of the ship: "))
        except ValueError:
            print('Not an appropriate choice, please select a valid row')
            continue
        else:
            break

    while True:
        try:
            column = input("Enter the column of the ship: ").upper()
            while column not in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                print('Not an appropriate choice, please select a valid column')
                column = input("Enter the column of the ship: ").upper()
        except ValueError:
            print('Not an appropriate choice, please select a valid column')
            continue
        else:
            break
    return row - 1, letters_to_numbers[column]


"""
check if all ships are hit
"""


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "~":
            print("You have already targeted that area!")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Lucky Shot!, Hit!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("HaHa! Nothing But Water, MISS!")
            GUESS_BOARD[row][column] = "~"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You Win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns, Game over!")

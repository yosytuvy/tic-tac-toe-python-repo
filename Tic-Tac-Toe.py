import random


def empty_indexes(bd):
    bd_empty = []
    empty = 0
    for i in bd:
        if i == ' ':
            bd_empty.append(empty)
        empty += 1
    return bd_empty


def shape_select():
    shape = input('select shape X/O: ')
    while shape != 'X' and shape != 'O':
        shape = input('please select only X/O: ')
    print('you are the', shape, 'shape')
    if shape == 'X':
        return shape, 'O'
    return shape, 'X'


def who_first():
    if random.randint(0, 1):
        return 'computer'
    return 'player'


def print_board(bd):
    print('\n')
    print('  ' + bd[1] + '|' + bd[2] + '|' + bd[3])
    print('---------')
    print('  ' + bd[4] + '|' + bd[5] + '|' + bd[6])
    print('---------')
    print('  ' + bd[7] + '|' + bd[8] + '|' + bd[9])


def computer_turn(bd, shape):
    empty_places = empty_indexes(bd)
    if len(empty_places) == 10:
        bd[1] = shape
        return bd
    elif empty_places.__contains__(5):
        bd[5] = shape
        return bd


def player_turn(bd, shape):
    empty_places = empty_indexes(bd)
    player_choice = int(input("you turn: "))
    while not empty_places.__contains__(player_choice):
        player_choice = int(input("enter a empty place: "))
    bd[int(player_choice)] = shape
    return bd




board = [' '] * 10
player_shape, computer_shape = shape_select()
first = who_first()
print('the ' + first + ' go first')
print_board(board)
moves = 10
if first == 'computer':
    board = computer_turn(board, computer_shape)
    print_board(board)
    moves -= 1
for move in range(moves):
    board = player_turn(board, player_shape)
    print_board(board)
    board = computer_turn(board, computer_shape)
    print_board(board)
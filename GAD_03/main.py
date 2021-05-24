table = 9 * [0]

symbols = {
    0: '.',
    1: 'X',
    2: 'O'
}


def reset_table():
    for i in range(9):
        table[i] = 0


def set_x(x, y):
    pos = x * 3 + y
    if table[pos] != 0:
        return False
    table[pos] = 1
    return True


def set_o(x, y):
    pos = x * 3 + y
    if table[pos] != 0:
        return False
    table[pos] = 2
    return True


def print_table(table=table):
    print(r'| {} | {} | {} |'.format(symbols[table[0]], symbols[table[1]], symbols[table[2]]))
    print(r'| {} | {} | {} |'.format(symbols[table[3]], symbols[table[4]], symbols[table[5]]))
    print(r'| {} | {} | {} |'.format(symbols[table[6]], symbols[table[7]], symbols[table[8]]))


def check_winner(table=table):
    for x in range(3):
        if table[x * 3] == table[x * 3 + 1] == table[x * 3 + 2] != 0:
            return table[x * 3]
    for x in range(3):
        if table[x] == table[3 + x] == table[6 + x] != 0:
            return table[x]
    if table[0] == table[4] == table[8] != 0:
        return table[0]
    if table[2] == table[4] == table[6] != 0:
        return table[2]
    for i in table:
        if i == 0:
            return -1
    return 0


def get_best_move(table):
    table = table.copy()
    best_score = -1
    move = -1
    for i in range(9):
        if table[i] == 0:
            table[i] = 2
            score = min_max(table, True)
            if score > best_score:
                move = i
                best_score = score
            table[i] = 0

    return move


def min_max(table, player):
    table = table.copy()
    symbol = 1
    best_score = 1
    if not player:
        next_player = True
    else:
        next_player = False

    if not player:
        symbol = 2
        best_score = -1

    winner = check_winner(table)

    if winner == 0:
        return 0
    elif winner == 1:
        return -1
    elif winner == 2:
        return 1

    for i in range(9):
        if table[i] == 0:
            table[i] = symbol
            score = min_max(table, next_player)
            if player and (best_score > score):
                best_score = score
            if (not player) and (best_score < score):
                best_score = score
            table[i] = 0

    return best_score


if __name__ == "__main__":
    while True:
        reset_table()
        game_type = input('''Choose method:
        0. Vs Player
        1. Vs Bot
        2. Exit
        ''')

        try:
            game_type = int(game_type)
        except ValueError:
            print('Please insert one of the given numbers')
            continue

        if game_type < 0 or game_type > 3:
            print('Please insert one of the given numbers')
            continue

        if game_type == 2:
            break
        elif game_type == 0:
            player = True
            while check_winner() == -1:
                print_table()
                if player:
                    i = int(input("X: Insert line "))
                    j = int(input("X: Insert column "))
                    if not set_x(i, j):
                        print("invalid move")
                        continue
                    player ^= True
                else:
                    i = int(input("O: Insert line "))
                    j = int(input("O Insert column "))
                    if not set_o(i, j):
                        print("invalid move")
                        continue
                    player ^= True

            winner = check_winner()
            if winner <= 0:
                print("No one won")
            else:
                print("The winner is:", symbols[winner])
        else:
            player = True
            while check_winner() == -1:
                print_table()
                if player:
                    i = int(input("X: Insert line "))
                    j = int(input("X: Insert column "))
                    if not set_x(i, j):
                        print("invalid move")
                        continue
                    player ^= True
                else:
                    move = get_best_move(table)
                    table[move] = 2
                    player ^= True

            print_table()
            winner = check_winner()
            if winner <= 0:
                print("No one won")
            else:
                print("The winner is:", symbols[winner])

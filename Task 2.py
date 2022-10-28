# Создайте программу для игры с конфетами человек против человека.

def check(tab):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if tab[each[0]] == tab[each[1]] == tab[each[2]]:
            return tab[each[0]]
    return False


def input_data(player_token, tab):
    valid = False
    while not valid:
        player_answer = input("Choose position " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Incorrect position")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(tab[player_answer-1]) not in "XO"):
                tab[player_answer-1] = player_token
                valid = True
            else:
                print("Position is taken")
        else:
            print("Incorrect value. Choose 1 to 9.")


def print_tab(tab):

    for i in range(3):
        print("  |", tab[0+i*3], " | ", tab[1+i*3], " | ", tab[2+i*3], " | ")


def main(tab):
    counter = 0
    win = False
    while not win:
        print_tab(tab)
        if counter % 2 == 0:
            input_data("X", tab)
        else:
            input_data("O", tab)
        counter += 1
        if counter > 4:
            tmp = check(tab)
            if tmp:
                print(tmp, "Win!")
                win = True
                break
        if counter == 9:
            print("Tie!")
            break


tab = list(range(1, 20))
main(tab)

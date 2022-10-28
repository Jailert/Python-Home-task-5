# Создайте программу для игры в ""Крестики-нолики"".

from random import randint


def input_dat(name):
    x = int(input(f"{name} Take from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name} Enter correct number: "))
    return x


def p_print(name, k, counter, value):
    print(f"{name} took {k} now have {counter}. {value} left.")


def bot_calc(value):
    k = randint(1, 29)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k


player1 = "Player"
player2 = "Bot"
value = int(input("Amount of candies: "))
first_turn = randint(0, 2)
if first_turn:
    print(f"{player1} first")
else:
    print(f"{player2} first")

counter1 = 0
counter2 = 0

while value > 28:
    if first_turn:
        k = input_dat(player1)
        counter1 += k
        value -= k
        first_turn = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        first_turn = True
        p_print(player2, k, counter2, value)

if first_turn:
    print(f"{player1} Won")
else:
    print(f"{player2} Won")

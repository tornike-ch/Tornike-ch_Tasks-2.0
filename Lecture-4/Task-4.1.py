from random import randint

number_of_players = int(input("შეიყვანეთ მონაწილეთა რაოდენობა: "))

if number_of_players > 0:
    for player in range(number_of_players):
        print(randint(1, 6), randint(1, 6))
else:
    exit(1)
from random import randint

user_number = int(input("შეიყვანეთ რიცხვი 1-დან 30-მდე: "))

number_list = []

if 0 < user_number < 30:
    for number in range(user_number):
        number_list.append(randint(0, 1000))
    print(number_list)
    print(max(number_list))
else:
    exit(1)
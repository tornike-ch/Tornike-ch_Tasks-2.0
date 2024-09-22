user_number = int(input("შეიყვანეთ რიცხვი 1-დან 1000-მდე: "))

divider_list = []

if 0 < user_number < 1000:
    for number in range(1, user_number+1):
        if user_number % number == 0:
            divider_list.append(number)
        else:
            pass
    print(divider_list)
else:
    exit(1)
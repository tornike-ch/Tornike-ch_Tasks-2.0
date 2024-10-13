user_number = int(input("შეიყვანე რიცხვი 1-დან 50-მდე: "))

counter = 0

if 0 < user_number < 50:
    for number in range(1, user_number + 1):
        count = 0
        print(f"{number} - ", end="")
        for divider in range(1, number + 1):
            if number % divider == 0:
                print(divider, end = " ")
                count += 1
            if count == 3:
                break
        print()
            
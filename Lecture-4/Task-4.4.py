user_number = int(input("შეიყვანეთ რიცხვი: "))

first_number = 0
second_number = 1
next_number = 1
sequence = [1]

if user_number > 0:
    for number in range(user_number):
        next_number = first_number + second_number 
        sequence.append(next_number)
        first_number = second_number
        second_number = next_number
    print(sequence[user_number-1])

"""
დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს.
პროგრამამ უნდა დაბეჭდოს ყველა მარტივი გამყოფი ერთ ხაზზე.
შემოსული რიცხვის მაქსიმალური მნიშვნელობაუნდა იყოს 10. 
მაგალითი: თუპროგრამას გადავეცით 6, გამოსავალზე უნდა დაიბეჭდოს 2, 3.
ახსნა: 6 იყოფა 2-ზეცდა 3-ზეც. 2 და 3 არის მარტივი რიცხვები.
დაიცავით პროგრამა ისეთი არგუმენტებისგან, რომლებიც არ არის დასაშვები.
"""
user_number = int(input("შეიყვანეთ რიცხვი 0-დან 10-ის ჩათვლით: "))

#Solution 1

if user_number in (0, 1):
    print("ამ რიცხვს არ აქვს მარტივი გამყოფი")
elif user_number in (2, 4, 8):
    print(2)
elif user_number in (3, 9):
    print(3)
elif user_number == 6:
    print(2, 3)
elif user_number == 5:
    print(5)
elif user_number == 7:
    print(7)
elif user_number == 10:
    print(2,5)
else:
    print("არასწორი ციფრი")
    exit(1)


#Solution 2

if user_number < 0 or user_number > 10:
    print("დაფიქსირდა შეცდომა")
    exit(1)
else:
    dividers = []
    for number in range(2, 10):
        if user_number % number == 0:
            if number in (2, 3, 5, 7):
                dividers.append(number)
    for digit in dividers:
        print(digit, end=" ")


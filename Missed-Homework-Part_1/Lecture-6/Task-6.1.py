"""
დაწერეთ პროგრამა რომელიც “ჩაიფიქრებს” მთელ რიცხვს 0-დან 100-მდე.
Მომხმარებელმა უნდა შემოიყვანოს თავისი ვარიანტი ჩაფიქრებული რიცხვის.
Თუ მომხმარებლის შემოყვანილი რიცხვი დაემთხვა პროგრამის ჩაფიქრებულ რიცხვს,
დაბეჭდეთ You are winner. Თუ მომხმარებლის შემოყვანილი რიცხვი მეტია,
კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ high. თუ მომხმარებლის შემოყვანილი
რიცხვი ნაკლებია კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ low.
Მომხმარებელს აქვს მაქსიმუმ 10 მცდელობა. Თუ მომხმარებელმა 10 მცდელბაში 
ვერ გამოიცნო რიცხვი, დაბეჭდეთ Computer is winner.
"""
from random import randint
comp_num = randint(1, 100)
counter = 1


while counter < 10:
    user_num = int(input("შეიყვანე რიცხვი 1-დან 100-მდე: "))
    counter += 1
    if user_num == comp_num:
        print("You are winner")
        break
    elif user_num > comp_num:
        print("High")    
    else:
        print("Low")

if counter == 10 and user_num != comp_num:
    print("Computer is winner")
    
    

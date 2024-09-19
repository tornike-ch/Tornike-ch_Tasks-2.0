from datetime import datetime

day = int(input("შეიყვანეთ თქვენი დაბადების რიცხვი: ")) 
month = int(input("შეიყვანეთ თქვენი დაბადების თვის რიცხვითი მნიშვნელობა: "))  
year = int(input("შეიყვანეთ თქვენი დაბადების წლის რიცხვითი მნიშვნელობა: "))  
weekdays = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"]
number_of_days = 31

if 1 <= month <= 12:
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            number_of_days = 29
        else:
            number_of_days = 28
    elif month in (4, 6, 9, 11):
        number_of_days == 30
    else:
        number_of_days == 31
    
    if 1 <= day <= number_of_days:
        birth_day = datetime(year, month, day)
        day_of_week = birth_day.weekday()
        print(weekdays[day_of_week])
    else:
        exit(1)
else:
    exit(1)

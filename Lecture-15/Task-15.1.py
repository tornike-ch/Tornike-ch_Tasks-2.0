"""
Დააგენერირეთ 100 ცალი შემთხვევითი რიცხვი. 
გააკეთეთ ლექსიკონი ორი გასაღებით even და odd, 
მათი მნიშნველობა უნდა იყოს ლუწი და კენტი რიცხვების რაოდენობები დაგენერირებული 100 რიცხვიდან.
"""
from random import randint

count_even = 0
count_odd = 0

for _ in range(100):
    number = randint(1, 100000000)
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

odds_and_evens = {
    "even":count_even,
    "odd":count_odd
}

print(odds_and_evens)
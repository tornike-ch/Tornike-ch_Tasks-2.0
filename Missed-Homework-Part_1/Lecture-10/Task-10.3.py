"""
Დაწერეთ ფუნქცია რომელიც დაითვლის რიცხვის ფაქტორიალს.
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def factorial(n):
    counter = 0
    num_fact = 0
    while counter < n + 1:
        num_fact += counter
        counter += 1
    print(num_fact)

factorial(5)
factorial(3)
factorial(7)
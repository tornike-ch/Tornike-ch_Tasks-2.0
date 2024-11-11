"""
6. Დაწერეთ ფუნქცია რომელსაც გადაეცემა მანქანის მწარმოებელი და გამოშვების წელი.
Მანქანის მწარმოებელი უნდა იყოს აუცილებელი არგუმენტი
ხოლო გამოშვების წელის ნაგულისხმევი მნიშვნელობა უნდა იყოს მიმდინარე წელი.
Ფუნქციას უნდა ჰქონდეს შესაძლებლობა, რომ გადაეცეს განუზღვრელი დასახელების
და რაოდენობის კონფიგურაციის პარამეტრები.
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def car(company, year = 2024, *args):
    features = ", ".join(args)
    if not args:
        print(f"your car is made by {company}, it was released in year {year}.")
    if args:    
        print(f"your car is made by {company}, it was released in year {year}. The car comes with {features}.")

car("Toyota", 2020, "abs", "airbags", "heated seats")
car("Mercedes")
car("BMW", 2023)
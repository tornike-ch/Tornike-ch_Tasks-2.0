"""
Დაწერეთ ფუნქცია რომელსაც გადაეცემა ტექტი და აბრუნებს ამ ტექსტს 
შებრუნებული მიმდევრობით. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა
არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def reverse_text(word):
    print(word[::-1])

reverse_text("Hello")
reverse_text("World")
reverse_text("Hello World")
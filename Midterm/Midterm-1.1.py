"""
1. (5 ქულა) Დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები:
სახელი, გვარი, ასაკი და ქალაქი. Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში:
Hello სახელი გვარი. Age: ასაკი. City: ქალაქი.
"""

user_name = input("შეიყვანე შენი სახელი: ")
user_lastname = input("შეიყვანე შენი გვარი: ")
user_age = input("შეიყვანე შენი ასაკი: ")
user_city = input("შეიყვანე ქალაქი: ")

print(f"Hello {user_name} {user_lastname}. Age: {user_age}. City: {user_city}")
"""
3. (12 ქულა) Დაწერეთ თამაში rock, paper, scissor.
Დაწერეთ ფუნქცია რომელიც დააგენერირებს შემთხვევითად ერთ-ერთ სიმბოლოს ჩამოთვლილი სამიდან R,P,S.
Დაწერეთ მეორე ფუნქცია main, რომელშიც მომხმარებელს შეაყვანინებთ თავის არჩევანს R, P ან S.
სიმარტივისთვის შეგიძლიათ უგულებელყოთ ყველა შემოწმება მომხმარებლის ინფუთზე.
Შეადარეთ ერთმანეთს მომხმარებლის შემოყვანილი სიმბოლო და თქვენი ფუნქციის
დაგენერირებული სიმბოლო და გამოავლინეთ გამარჯვებული.
Წესები: R ამარცხებს S S ამარცხებს P P ამარცხებს R P P, R R, S S
არის ფრე იმ შემთხვევაში თუ გვაქვს ფრე, უნდა მისცეთ კიდევ ერთი თამაშის საშუალება.
"""

from random import randint
user_choice = input("აირჩიე ქვა - R, ქაღალდი - P ან მაკრატელი - S: ")

def main():
    if user_choice == "R" or user_choice == "r":
        return 1
    elif user_choice == "P" or user_choice == "p":
        return 2
    elif user_choice == "S" or user_choice == "s":
        return 3
    else:
        return "Wrong symbol"


comp_choice = randint(1, 3)

counter = 1

while counter > 0:
    if main() == comp_choice:
        comp_choice = randint(1, 3)
        print("ფრე")
        user_choice = input("აირჩიე ქვა - R, ქაღალდი - P ან მაკრატელი - S: ")
    else:
        counter = 0
        if main() == 1:
            if comp_choice == 3:
                print("შენ გაიმარჯვე")
            else:
                print("შენ დამარცხდი")
        elif main() == 2:
            if comp_choice == 1:
                print("შენ დამარცხდი")
            else:
                print("შენ გაიმარჯვე")
        else:
            if comp_choice == 1:
                print("შენ დამარცხდი")
            else:
                print("შენ გაიმარჯვე")
first_word = input("შეიყვანეთ პირველი სიტყვა: ").lower()
second_word = input("შეიყვანეთ მეორე სიტყვა: ").lower()

first_letters = []
second_letters = []

for letter in first_word:
    if "{" > letter > "`":
        first_letters.append(letter)

for letter in second_word:
    if "{" > letter > "`":
        second_letters.append(letter)

if sorted(first_letters) == sorted(second_letters):
    print("Yes")
else:
    print("No")
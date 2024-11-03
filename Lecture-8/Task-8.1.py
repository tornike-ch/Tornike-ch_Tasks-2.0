user_word = input("შეიყვანეთ შესამოწმებელი სიტყვა: ").lower()

user_letters = []

for letter in user_word:
    if "{" > letter > "`":
        user_letters.append(letter)
        print(user_letters)

if user_letters == list(reversed(user_letters)):
    print("Is a palindrome")
else:
    print("Is not a palindrome")
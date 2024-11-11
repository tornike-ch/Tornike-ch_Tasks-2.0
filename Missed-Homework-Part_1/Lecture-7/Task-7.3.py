"""
პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო,
პირველი და შუა ასოები 5-ჯერ while ლუპით.
თუ შემოყვანილი ტექსტის ზომა არის ლუწი, მაშინ პროგრამამ უნდა დაბეჭდოს შუა ორი სიმბოლო.
"""

user_word = input("შეიყვანეთ სიტყვა: ")
user_word_len = len(user_word) - 1
counter = 0
middle_char = 0
while counter < 5:
    counter += 1
    middle_char = user_word_len // 2
    if len(user_word) % 2 == 0:
        print(f"პირველი ასოა: {user_word[0]}, ბოლო ასოა: {user_word[user_word_len]}, შუა ასოებია: {user_word[middle_char : middle_char + 2]}")
    else:
        print(f"პირველი ასოა: {user_word[0]}, ბოლო ასოა: {user_word[user_word_len]}, შუა ასოა: {user_word[middle_char]}")
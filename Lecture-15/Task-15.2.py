"""
Დაწერეთ პროგრამა რომელიც მიიღებს სტრიქონს.
Პროგრამამ უნდა დაითვალოს ამ სტრიქონში არსებული სიმბოლოები რომელი რამდენჯერ გვხვდება და დაბეჭდოს ეკრანზე.
"""
user_word = input("შეიყვანეთ სტრინგი: ").lower()

char_count = {}

for char in user_word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

print(char_count)
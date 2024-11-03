"""
დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 10000
და დაბეჭდავს ამ რიცხვის შებრუნებულ მნიშვნელობას და ამ რიცხვში შემავალი ციფრების ჯამს.
გამოიყენეთ while ციკლი
"""

user_num = int(input("შეიყვანეთ რიცხვი 1-დან 10000-მდე: "))
reversed_number = 0
digit_sum = 0

while user_num > 0:
    digit = user_num % 10
    reversed_number = reversed_number * 10 + digit
    digit_sum += digit
    user_num = user_num // 10

print(f"შებრუნებული რიცხვი: {reversed_number}")
print(f"ციფრების ჯამი: {digit_sum}")
    


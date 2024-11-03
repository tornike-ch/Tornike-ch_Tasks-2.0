"""
პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა.
დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი.
"""

user_str = input("შეიყვანეთ string-ი: ")
counter = 1

while counter < len(user_str):
    if user_str[counter] != "e":
        print(user_str[counter], end="")
    counter += 2
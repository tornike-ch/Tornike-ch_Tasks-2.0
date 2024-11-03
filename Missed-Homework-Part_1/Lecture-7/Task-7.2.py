#პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ სიტყვიდან მხოლოდ თანხმოვანი ასოები.

user_str = input("შეიყვანე სიტყვა: ")
vowels = "aeiouAEIOU"

for char in user_str:
    if char not in vowels:
        print(char, end=" ")
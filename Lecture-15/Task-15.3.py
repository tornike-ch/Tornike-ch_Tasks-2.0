"""
Დაწერეთ პროგრამა რომელიც მიიღებს ინფორმაციას ვის ვინ დაუმეგობრდა.
Თუ პროგრამამ მიიღო სიტყვა FINISH, უნდა დაასრულოს მუშაობა.
Თუ პროგრამამ მიიღო სიტყვა Giorgi – Nini, ნიშნავს რომ Nini დაუმეგობრდა Giorgi-ს და Giorgi დაუმეგობრდა Ninis.
Პროგრამამ მუშაობის დასრულების წინ, ეკრანზე უნდა დაბეჭდოს ვინ ვისი მეგობარია.
"""
pairs={}

while True:
    friends = input("შეიყვანე ვინ ვის დაუმეგობრდა: ").lower()

    if friends == "FINISH".lower():
        break

    else:
        first_friend, second_friend = friends.split(" - ")
        if first_friend not in pairs:
            pairs[first_friend] = []
        if second_friend not in pairs[first_friend]:
            pairs[first_friend].append(second_friend)
        if second_friend not in pairs:
            pairs[second_friend] = []
        if first_friend not in pairs[second_friend]:
            pairs[second_friend].append(first_friend)

print(pairs)

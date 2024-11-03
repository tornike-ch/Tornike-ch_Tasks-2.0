"""
Დაწერეთ ფუნქცია, რომელიც დაადგენს გადაცემული რიცხვი მარტივია თუ არა.
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def simple(n):
    counter = 0
    for num in range(1, n + 1):
        if n % num == 0:
            counter += 1
    if counter <= 2:
        print("მარტივი")
    else:
        print("რთული")

simple(13)
simple(9)
simple(2)
simple(21)
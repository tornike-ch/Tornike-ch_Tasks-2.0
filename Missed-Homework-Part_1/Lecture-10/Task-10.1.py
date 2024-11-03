"""
Დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს ტექსტს და 
დაარუნებს ამ ტექსტში ხმოვნების რაოდენობას.
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def vowles(word):
    counter = 0
    vowles = "aeiouAEIOU"
    for char in word:
        if char in vowles:
            counter += 1
    print(counter)

vowles("Hello World!")

vowles("AbCdeFGHIjklmnOPQRstuvWxyz")

vowles("AbgdevZTIklmnOPJRstufqRyshchCZwkhjh")
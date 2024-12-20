"""
დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1.
პროგრამამ უნდა დაითვალის რიცხვი x და დაბეჭდოს ეკრანზე.
Რიცხვი x ის დათვლის პრინციპი ასეთია.
x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )
გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 10000, 100000. რას ამჩნევთ?
"""

n = int(input("შეიყვანეთ ნატურალური რიცხვი: "))
x = 0

for num in range(n):
    x += (-1) ** num / (2 * num + 1)
x *= 4

print(x)
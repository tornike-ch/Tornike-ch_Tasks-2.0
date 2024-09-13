import math

triangle_sides = input("შეიყვანეთ სამკუთხედის გვერდების სიგრძეები: ")

a = int(str.split(triangle_sides)[0])
b = int(str.split(triangle_sides)[1])
c = int(str.split(triangle_sides)[2])
p = a + b + c
s = p / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"აღნიშნული სამკუთხედის პერიმეტრია: {p}, ფართობი კი: {area}")
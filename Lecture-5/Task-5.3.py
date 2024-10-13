n = int(input("შეიყვანეთ რიცხვი 1-დან 20-მდე: "))

if 0 <= n < 20:
    a = 0
    b = 1
    i = 0
    while i <= n:
        if i == 0:
            print(a, end=' ')
        elif i == 1:
            print(b, end=' ')
        else:
            c = a + b
            print(c, end=' ')
            a = b
            b = c
        i += 1
else:
    print("თქვენ მიერ შეყვანილი რიცხვი არ აკმაყოფილებს მოთხოვნებს")

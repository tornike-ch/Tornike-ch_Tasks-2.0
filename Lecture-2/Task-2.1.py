"""
1. Დაწერეთ პროგრამა რომელიც მიიღებს true ან false. Თუ პროგრამამ მიიღო true, ეკრანზე დაბეჭდეთ “whoala”. 
"""

true_or_false = input("დაწერე true ან false: ")

if true_or_false == "true" or true_or_false == "false":
    if true_or_false == "true":
        print("whoala")
    else:
        exit
else:
    print("პასუხი არ შეესაბამება მოთხოვნას")
    exit(1)
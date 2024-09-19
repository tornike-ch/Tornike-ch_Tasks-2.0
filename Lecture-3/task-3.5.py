import datetime
from forex_python.bitcoin import BtcConverter


day = int(input("ბიტკოინის ყიდვის დღე: ")) 
month = int(input("ბიტკოინის ყიდვის თვე: "))  
year = int(input("ბიტკოინის ყიდვის წელი "))
cost = int(input("რამდენი დოლარი გადაიხადეთ ბიტკოინში? (დაწერეთ რიცხვითი მნიშვნელობა) "))
number_of_days = 31

if 1 <= month <= 12:
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            number_of_days = 29
        else:
            number_of_days = 28
    elif month in (4, 6, 9, 11):
        number_of_days == 30
    else:
        number_of_days == 31
else:
    exit(1)



b = BtcConverter()

date_obj = datetime.datetime(year, month, day)

purchase_price = b.get_previous_price('EUR', date_obj)

purchace_amount = cost / purchase_price

current_price_in_usd = b.convert_btc_to_cur(purchace_amount, 'USD')

if current_price_in_usd > 0:
    print(current_price_in_usd)
else:
    exit(1)


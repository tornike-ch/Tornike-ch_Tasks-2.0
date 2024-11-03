time = "2024-03-22T19:17:42.956376+00:00"

year = time[0:4]
month = time[5:7]
day = time[8:10]
hour = int(time[11:13])
minute = time[14:16]
second = time[17:19]
plus_or_minus = time[-6]
time_zone = int(time[-5:-3])

if hour > 12:
    hour -= 12

print(f"{day}-{month}-{year} {hour}:{minute}:{second} {plus_or_minus}{time_zone}")


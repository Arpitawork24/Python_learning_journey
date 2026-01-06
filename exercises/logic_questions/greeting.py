import time

#get current time components
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

print("current time:", time.strftime('%H:%M:%S'))
if (hour > 5) or (hour == 5 and min >= 0):
    if hour < 12:
        print("Good Morning!")
    elif hour < 17:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
else:
    print("Good Evening!")

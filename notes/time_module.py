import time

def usingwhile():
    i = 0
    while i < 10:
        print(i)
        i = i+1

def usingfor():
    for i in range(10):
        print(i)

start1 = time.time()
usingwhile()
end1 = time.time()
usingfor()
end2 = time.time()

print(end1 - start1)
print(end2 - end1)

t1 = time.time()
print(4)
time.sleep(5)
print("printed 4")
t2 = time.time()
print(t2 - t1)

# time.localtime() returns the current time based on your system clock.
# It does not return a simple number or string.
# It returns a time object (structure) containing many parts of the date.
t = time.localtime()
# strftime means: string format time
formatted_time = time.strftime("%Y-%m-%d  %H:%M:%S", t)
print(formatted_time)
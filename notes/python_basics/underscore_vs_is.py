# py when creates 2 same files then also save at diff locations 
# so only data structures that are mutable like list are save at diff locations eg- string, int, tuple
# mutables are saved at diff locations like eg - lists , sets
a = {50000}  # or [500]
b = {50000}  # or [500]

if a is b:  # compare exact location of object in memory
    print(True)
else:
    print(False)
    
if a == b:  # compare values only
    print(True)
else:
    print(False)
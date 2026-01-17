# we can raise custom errors using raise keyword
# errors are raised to prevent further errors in code

# for eg if the num is not between 5 nd 9 nd further code has the eligibility of that only then it will create error at that time nd code will give error due to this thats why we take precautions if the input doesn't come accordingly nd we raise custom errors

n = int(input("enter num= "))
if (n<5 or n>9):
    raise ValueError ("num should be between 5 and 9")
else:
    print(n)
#default arguments-

def average(a=9,b=2): #a nd b has default values
    return (a+b)/2
print(average(5))  #here a=5 nd b has default value i.e. b=2
print(average(b=4)) #here b=4 nd a has default value i.e. a=9

# keywword arguments-
# *args - non keyword arguments
# *kwargs - keyword arguments

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for word in args:
        print(word)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items(): #items is a built-in dictionary method
        print(f"{key} == {value}") #f-string (formatted string)

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Rohit', mid='Prakash', last='Sharma')

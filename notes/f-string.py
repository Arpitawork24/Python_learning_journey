# .format() way
intro = "Hey I am {} nd my age is {}"
name = "xyz"
age = 20
print("in .format way \n",intro.format(name, age))
print(intro.format("abc", age))

# f-string way
intro1 = f"Hey I am {name} nd my age is {age}" #used default name nd age values from above
print("in f-string way \n",intro1)

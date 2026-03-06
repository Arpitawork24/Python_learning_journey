# walrus operator (:=) allows u to assign value to a variable within an expression.
# it can be used in while loops nd if statements.
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())
    
names = ["arpita", "sanu", "piyu"]
if (name := input("enter ur name - ")) in names :
    print("hello ", name)
else :
    print("name not found")
#kbc game
print("hello")
t_m =0
q1 = "q1 - capital of gujarat"
print(q1)
print ("options are \nA- gandhinagar , \nB- jaipur")
ans = input("answer a,b,c,d ?? = ").lower()
# input() returns the users value
# print() only displays and returns None
# ans = print(input()) stores None, not the input
# Always store input() directly


if ans == "a":
    print("right")
    t_m +=1000
else :
    print("wrong")
    
q2 = print("\nQ2. What is the colour of the sky?")
print ("options are \nA- pink , \nB- blue")
ans = input("answer a,b,c,d ?? = ").lower()
if ans == "b":
    print("right")
    t_m +=100
else :
    print("wrong")
    
print("total score - " ,t_m)

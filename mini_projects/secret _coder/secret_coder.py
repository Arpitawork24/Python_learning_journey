import random
import string

def show_menu():
    print("secret coder")
    print("1. code")
    print("2. decode")

def main():
    while True:
        show_menu()
        choice = int(input("select 1 or 2= " ))
        
        if choice == 1:
            code()
        elif choice == 2:
            decode()
        else:
            print("wrong choice")


def code():
    word = input("enter the word= ")
    if word == "":
        print("empty")
        return
    elif len(word)<3:
        word = word[::-1]
        print(word)
    else :
        temp = word[1:] + word[0]
        front_random = ''.join(random.choices(string.ascii_lowercase, k=3))
        back_random = ''.join(random.choices(string.ascii_lowercase, k=3))
        result = front_random + temp + back_random
        print(result)
    

def decode():
    word = input("enter the word= ")
    if word == "":
        print("empty")
        return
    elif len(word)<3:
        word = word[::-1]
        print(word)
    else :
        temp = word[3:-3]
        word = temp[-1] + temp[0:-1]
        print(word)

main()
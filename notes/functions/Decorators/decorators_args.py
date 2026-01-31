def greet (fx):
    def mfx(*args ,**kwargs):
        print("welcome")
        result = fx(*args,  **kwargs)
        print("thank u")
        return result
    return mfx

@greet
def summ(a,b):
    print(f"{a} + {b} = {a+b}")

summ(2,3)
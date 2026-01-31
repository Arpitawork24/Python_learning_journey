# A decorator is a function that takes another function and adds extra behavior to it.
# eg - here greet is a decorator.

def greet (fx):
    def mfx():
        print("welcome")
        fx()
        print("thank u")
    return mfx

@greet
def hello():
    print("hello world")

hello()

    
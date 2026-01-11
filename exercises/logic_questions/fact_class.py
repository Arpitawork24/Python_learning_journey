class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        if n == 0:
            return 1
        else :
            return n*self.factorial(n-1) #Its self.factorial because factorial is a method inside a class, not a standalone function.

#self is used to call a class method from within the same class because the method belongs to the object, not the global scope.
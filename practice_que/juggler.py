class Solution:
    def jugglerSequence(self, n):
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = int(n ** 0.5)
            else:
                n = int(n ** 1.5)
            seq.append(n)
        return seq


# only for VS Code testing
n = int(input())
print(Solution().jugglerSequence(n))

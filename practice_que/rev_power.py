# # for gfg
# class Solution:
#     def reverseexponentiation(self, n):
#         # code here
#         temp = n
#         rev =0
#         while temp >0:
#             rev = rev*10 + (temp%10)
#             temp = temp//10
        
#         return n**rev

# for vs-
class Solution:
    def reverseexponentiation(self, n):
        rev = 0
        temp = n

        # reverse the number
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10

        # n raised to the power of its reverse
        return n ** rev


# ---- input & execution part ----
n = int(input("Enter number: "))

obj = Solution()
result = obj.reverseexponentiation(n)

print(result)

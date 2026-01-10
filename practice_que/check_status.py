# Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

# Return True for the following cases:

# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.
# Otherwise, return False.

#for gfg
# class Solution:
#     def checkStatus(self, a, b, flag):
#         # code here
#         if flag == False :
#             if (a>0 and b<0) or (a<0 and b>0) :
#                 return True
#             else :
#                 return False
#         elif flag == True:
#             if a<0 and b<0:
#                 return True
#             else :
#                 return False
#         else :
#             return False

# for vs code studio or any compiler -
class Solution:
    def checkStatus(self, a, b, flag):
        if flag == False:
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                return True
            else:
                return False

        elif flag == True:
            if a < 0 and b < 0:
                return True
            else:
                return False

        else:
            return False


# ---- INPUT ----
a = int(input("Enter a: "))
b = int(input("Enter b: "))
flag_input = input("Enter flag (True/False): ").lower()

# convert string to boolean SAFELY
if flag_input == "true":
    flag = True
elif flag_input == "false":
    flag = False
else:
    print("Flag must be True or False")
    exit()

obj = Solution()
print(obj.checkStatus(a, b, flag))


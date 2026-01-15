class Solution:
    def majorityElement(self, arr):
        #code here
        n = len(arr)
        freq={}
        for i in range(n):
            if arr[i] in freq :
                freq[arr[i]]+=1
            else:
                freq[arr[i]] = 1
        if freq[arr[i]] > n//2:
            return arr[i]
        return -1

# correct way to call
obj = Solution()
print(obj.majorityElement([2,3,2,2,6,2]))
# https://leetcode.com/problems/product-of-array-except-self/
 

"""
O(n^2)
class Solution(object):
    def productExceptSelf(self, nums):
 
        sol = []
        for index, value in enumerate(nums):
            no = nums[:]
            del no[index]
            mul = 1
            for ind,val in enumerate(no):
                mul*=val
            sol.append(mul)
        return sol
        

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in sol:
                return [i, sol[diff]]
            
            sol[num] = i
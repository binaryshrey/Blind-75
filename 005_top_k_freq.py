# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):

    def freq(self, nums):
        freq_map = {}
        for index, value in enumerate(nums):
            if value in freq_map:
                freq_map[value] += 1
            else:
                freq_map[value] = 1
        return freq_map

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_map = self.freq(nums)
        top_freq = sorted(frequency_map, key = frequency_map.get, reverse = True)
        return top_freq[:k]
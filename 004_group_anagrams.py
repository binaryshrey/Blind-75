# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = []
        mp = {}
        for index, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            
            if sorted_word in mp:
                mp[sorted_word].append(word)
            else:
                mp[sorted_word] = [word]
        for key,values in mp.items():
            anagrams.append(values)

        return anagrams
#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged_string = []
        i=j=0

        while i < len(word1) and j < len(word2) :
            merged_string.append(word1[i])
            merged_string.append(word2[j])
            i+=1
            j+=1

        if i < len(word1) :
            merged_string.extend(word1[i:])
        if j < len(word2) :
            merged_string.extend(word2[j:])

        return ''.join(merged_string)
        
# @lc code=end


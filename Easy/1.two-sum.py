#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Started a dictionary similar to hash map
        myDict={}

        # Going through eachNum
        for index , eachNum in enumerate(nums):
            
            # Calculating the reminder
            rem = target - eachNum

            if rem in myDict.keys():
                return [myDict[rem] , index]

            myDict[eachNum] = index

        
# @lc code=end


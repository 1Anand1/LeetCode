#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Follow up: Could you solve it without converting the integer to a string?

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if str(abs(x))[::-1]==str(abs(x)) and x>=0:
            return True
        else:
            return False

# @lc code=end


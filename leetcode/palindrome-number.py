#https://leetcode.com/problems/palindrome-number/
# Author: Lukas Rasocha
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        L = list(str(x))[::-1]

        s = ""
        for i in L:
            s = s+i

        return s == str(x)

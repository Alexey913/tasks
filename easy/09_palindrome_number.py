# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        for i in range(len(string)//2):
            if string[i] != string[- i - 1]:
                return False 
        return True
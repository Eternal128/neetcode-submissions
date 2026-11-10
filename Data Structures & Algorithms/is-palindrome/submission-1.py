class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets = "".join([char.lower() for char in s if char.isalnum()])
        return alphabets == alphabets[::-1]

        
        
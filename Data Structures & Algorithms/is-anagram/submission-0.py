class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            dict1 = {}
            for letter in s:
                if letter in dict1:
                    dict1[letter] += 1
                else:
                    dict1[letter] = 1
            
            for letter in t:
                if letter in dict1:
                    dict1[letter] -= 1
                else:
                    return False

            return all(count == 0 for count in dict1.values())
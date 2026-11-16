class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        pairs = {'[' : ']', '(' : ')', '{' : '}'}

        for i, letter in enumerate(s):
            if letter == "(" or letter == "{" or letter == '[':
                lst.append(letter)
            if letter == ")" or letter == "}" or letter == ']':
                if len(lst) == 0:
                    return False
                else:
                    removed = lst.pop()
                    if letter != pairs[removed]:
                        return False

        return len(lst) == 0
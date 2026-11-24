class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        # loop over the letters in the word to build the path
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True


    def search(self, word: str) -> bool:
        current = self.root
        # traversing the node for each character in the word
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True
        


# insert
# "cat"

# c a t
# retrun nothing


# search
# "cat"

# c -> a -> t
# return True

# search
# "car"

# c -> a 
# but r i missing
# return false


# root
#  |
#  c
#  |
#  a
#  | 
#  t 

# self.words = []

# self.words.append(word)


# for w in self.words:
#     if w.startWith(prefix): 
#         return True
    
# return False






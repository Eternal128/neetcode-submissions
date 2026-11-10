from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s)) #sorted word becomes the key to the group
            groups[key].append(s) # make it a dictionary
        return list(groups.values()) # return the values of the groups list as a list
        
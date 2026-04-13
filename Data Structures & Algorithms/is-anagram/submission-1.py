class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # loop through s and t and add chars to hash map
        # check if chars are the same
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        for c in sMap:
            if sMap[c] != tMap.get(c, 0):
                return False

        return True
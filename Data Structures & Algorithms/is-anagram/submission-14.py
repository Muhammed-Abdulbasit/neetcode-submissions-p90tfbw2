class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        if len(s) != len(t):
            return False
        
        for c in range(len(s)):
            sMap[s[c]] = sMap.get(s[c], 0) + 1
            tMap[t[c]] = tMap.get(t[c], 0) + 1
        
        for i in sMap:
            if sMap[i] != tMap.get(i, 0):
                return False
        return True
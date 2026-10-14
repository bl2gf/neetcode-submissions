class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = self.buildMap(s)
        tMap = self.buildMap(t)
        return sMap == tMap
        
    def buildMap(self, s: str):
        sMap = {}
        for c in s:
            if c in sMap:
                sMap[c] +=1
            else:
                sMap[c] = 1
        return sMap
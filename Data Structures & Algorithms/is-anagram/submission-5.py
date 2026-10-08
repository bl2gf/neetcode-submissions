class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqueS = {}
        uniqueT = {}
        for i in s:
            if i not in uniqueS:
                uniqueS[i] = 1
            else:
                uniqueS[i] +=1
        for i in t:
            if i not in uniqueT:
                uniqueT[i] = 1
            else:
                uniqueT[i] +=1
        return uniqueS == uniqueT
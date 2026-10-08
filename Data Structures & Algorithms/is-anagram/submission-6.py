class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        di = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dic[s[i]] = 1 + dic.get(s[i],0)
            di[t[i]] = 1 + di.get(t[i],0)
        return di == dic
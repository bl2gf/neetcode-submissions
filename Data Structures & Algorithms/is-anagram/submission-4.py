class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {} # where key = letter and value = times that letter appears
        tdict = {}
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[str(s[i])] =1
            if t[i] not in tdict:
                tdict[str(t[i])] =1
            if s[i] in sdict:
                sdict[str(s[i])] +=1
            if t[i] in tdict:
                tdict[str(t[i])] +=1
        return tdict == sdict
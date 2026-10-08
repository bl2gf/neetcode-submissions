class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        else:
            hashm =defaultdict(list)
            for s in strs:
                sor = "".join(sorted(s))
                hashm[sor].append(s)
            return list(hashm.values())
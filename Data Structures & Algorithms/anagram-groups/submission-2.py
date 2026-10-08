class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        else:
            hashm ={}
            result = []
            for s in strs:
                sor = "".join(sorted(s))
                if sor in hashm:
                    hashm[sor].append(s)
                else:
                    hashm[sor] = [s]
            for value in hashm.values():
                result.append(value)
            return result
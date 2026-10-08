class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        for i in strs:
            ordered_str = ''.join(sorted(i))
            print (ordered_str)
            if ordered_str not in anaDict:
                anaDict[ordered_str] = [i]
            else:
                anaDict[ordered_str].append(i)  
        return list(anaDict.values())
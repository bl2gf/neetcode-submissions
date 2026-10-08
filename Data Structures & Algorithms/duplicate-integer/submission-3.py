from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for item in nums:
            if item in duplicates:
                duplicates[item] += 1
                return True 
            else:
                duplicates[item] = 1
        return False
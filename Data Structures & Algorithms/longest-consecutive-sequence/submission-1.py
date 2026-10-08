class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        dict = {}
        for i in numSet:
            if (i-1) not in numSet:
                dict[i] = 1
                x = i
                while(x+1 in numSet):
                    dict[i] +=1
                    x+=1
        print(str(dict))
        return max(dict.values())

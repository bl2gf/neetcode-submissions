class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, number in enumerate(nums):
            if number > 0: #if in a sorted non-descending nums, the smallest value is >0, then nothing added in the list will = 0
                break
            if index > 0 and number == nums[index-1]: #means we've encountered a duplicate, skip
                continue
            
            l,r = index+1, len(nums) - 1
            while l < r :
                target = -number    
                if nums[l] + nums[r] > target:
                    r -=1 
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    res.append([number,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1                  
        return res
                
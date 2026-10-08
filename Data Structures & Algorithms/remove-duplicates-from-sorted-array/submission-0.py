class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k]=nums[i]
        return k+1 
        #since k is the index,we have to add one if we want
        #the actual number of unique elements.
        #bc unfortunately we count things from 1 
        #but arrays start at 0.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window = set() # create a set of unique values
        # L = 0 

        # for R in range(len(nums)):
        #     if R - L > k:
        #         window.remove(numsL) #invalid L index, remove from possibile pair of indices
        #         L+=1 #need to make it smaller bc abs(R-L) is bigger than k
        #     if nums[R] in window:
        #         return True
        #     windows.add(nums[R]) #we'd only get to this line if
        mp = {} #key is NumsValue=> value is Index 

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                #if value at i is a valid key in map and i - map[value] <= k 
                return True
            mp[nums[i]] = i 
            # 1->0
            # 2 ->1
            # 3-> 2
        return False
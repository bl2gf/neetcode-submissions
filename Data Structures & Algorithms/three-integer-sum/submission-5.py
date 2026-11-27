class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        print(nums)
        answer = []
        i = 0
        while i < len(nums)-2:
            if i != 0:
                if nums[i] == nums[i-1]:
                    i+=1 
                    continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                jk = nums[j] + nums[k]
                if jk == -nums[i]:
                    answer.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j]==nums[j+1]:
                        j+=1 #check that it doesn't matter if j +=1 or k -=1
                    j+=1
                if jk > -nums[i]:
                    k -= 1
                if jk < -nums[i]:
                    j += 1
            i+=1
        return answer

        # while i < len(nums):
        #     runningSum = nums[i] + nums[j]
        #     if runningSum < 0:
        #         j2 = j -1
        #         while j2 > 0:
        #             if nums[j2] + runningSum == 0:
        #                 answer.append([nums[i], nums[j], nums[j2]])
        #                 break
        #             if nums[j2] + runningSum < 0: # still less than 0, then moving back won't help
        #                 break
        #             j2 -= 1
        #     else: # runningSum >=0
        #         i2 = i+1
        #         while i2 < len(nums):
        #             if nums[i2] + runningSum == 0:
        #                 answer.append([nums[i], nums[j], nums[i2]])
        #                 break
        #             if nums[i2] + runningSum > 0: # still greater than 0, then moving forward won't help
        #                 break
        #             i2 += 1
        #     i+=1
        # return answer

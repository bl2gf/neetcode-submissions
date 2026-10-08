class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        result = []
        #where key = number and value = index
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain not in hashm:
                hashm[nums[i]] = i
            else:
                result.append(hashm[remain])
                result.append(i)
        return result
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        result = []
        for i in range(len(nums)):
            resultant = target - nums[i]

            if resultant in hashm:
                result.append(hashm[resultant])
                result.append(i)
            else:
                hashm[nums[i]] = i
        return result
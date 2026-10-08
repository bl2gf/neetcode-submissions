class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passedThru = {}
        result = []
        for i in range(len(nums)):
            difference = target - nums[i]
            print(difference)
            if difference not in passedThru:
                passedThru[nums[i]] = i
            else:
                result.append(passedThru[difference])
                result.append(i)
                return result
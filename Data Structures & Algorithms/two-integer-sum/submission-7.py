class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passedThru = {}
        result = []
        for index, value in enumerate(nums):
            diff = target - value
            if diff in passedThru:
                return [passedThru[diff], index]
            passedThru[value] = index
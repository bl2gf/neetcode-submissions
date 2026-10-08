class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        result = []
        for i in range(len(nums)):
            add = target - nums[i]
            print(add)
            if add in dict:
                result.append(dict[add])
                result.append(i)
                return result
            dict[nums[i]] = i
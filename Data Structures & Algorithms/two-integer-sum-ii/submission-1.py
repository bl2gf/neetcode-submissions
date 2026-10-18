class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            ijVal = numbers[i] + numbers[j]
            # print("ijVal is " + str(ijVal) + " for i: " + str(numbers[i]) + " and j: " + str(numbers[j]))
            if ijVal == target:
                return [i+1, j+1]
            elif ijVal > target:
                j -= 1
            else:
                i += 1
        
        return []
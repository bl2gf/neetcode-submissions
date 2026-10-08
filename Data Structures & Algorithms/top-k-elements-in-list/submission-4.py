class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqL = {}
        for num in nums:
            freqL[num] = freqL.get(num, 0) + 1
        a = sorted(freqL.items(), key= lambda pair: pair[1], reverse=True)
        result = []
        for i in range(k):
            result.append(a[i][0])
        return result
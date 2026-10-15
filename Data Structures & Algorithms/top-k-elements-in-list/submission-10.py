class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [None] * len(nums)
        counts = {}
        
        for i in nums:
            counts[i] = 1 + counts.get(i,0)

        for key in counts:
            count = counts[key]
            if freq[count - 1]:
                freq[count - 1].append(key)
            else:
                freq[count - 1] = [key]
        
        if nums == []:
            return []

        res = []
        i = len(freq) - 1
        while len(res) < k and i >= 0:
            if freq[i]:
                res.extend(freq[i])
            i -= 1
        
        return res
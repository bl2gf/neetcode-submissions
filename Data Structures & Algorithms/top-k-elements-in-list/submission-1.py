class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countingElems = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            if i not in countingElems:
                countingElems[i] = 1
            else: # if i is already in countingElems
                countingElems[i] += 1
        print(str(countingElems))
        for num, cnt in countingElems.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # countingElems = {}
        # bucket = [None]*len(nums)
        # for i in nums:
        #     if i not in countingElems:
        #         countingElems[i] = 1
        #     else: # if i is already in countingElems
        #         countingElems[i] += 1
        # print(str(countingElems))
        
        # #in the bucket, the index is the frequency and the value is the actual nums value
        # #in the dictionary, the KEY is the value from nums and the VALUE is the frequency
        # #thus bucket's index = frequency = dictionary's value
        # #bucket's value = actual nums value = dictionary key
        # for key in countingElems:
        #     bucket.insert(countingElems[key], key)
        # print(bucket)
        # counterOfK = k
        # result = []
        # for item in reversed(bucket):
        #     if k == 0:
        #         return result
        #     if item != None:
        #         result.append(item)
        #         k-=1
        # return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        ans = []
        for key in counts:
            val = counts[key]
            ans.append((val, key))
        ans.sort(reverse=True)
        ans = ans[:k]
        print(ans)
        for i in range(len(ans)):
            ans[i] = ans[i][1]
        return ans
        
        # sortedCounts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k])
        # print(sortedCounts)
        # answer = []
        # for key in sortedCounts:
        #     answer.append(key)

        return answer
        # countsArr = []
        # for key, value in counts:
        #     countsArr.append((value, key))

            
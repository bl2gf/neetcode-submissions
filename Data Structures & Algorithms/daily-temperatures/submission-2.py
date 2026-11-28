class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        unresolvedTemps = []
        for i, temp in enumerate(temperatures):
            # print(unresolvedTemps, temp)
            if len(unresolvedTemps) == 0:
                unresolvedTemps.append([i,temp])
                continue                
            if temp <= unresolvedTemps[-1][1]:
                unresolvedTemps.append([i,temp])
            if temp > unresolvedTemps[-1][1]:
                while temp > unresolvedTemps[-1][1]:
                    topElement = unresolvedTemps.pop()
                    result[topElement[0]] = i - topElement[0]
                    if len(unresolvedTemps) == 0:
                        break
                unresolvedTemps.append([i,temp])
        return result


        # result = []
        # for i, originalTemp in enumerate(temperatures):
        #     result.append(0)
        #     if i == len(temperatures) - 1:
        #         continue
        #     for index, temp in enumerate(temperatures[i+1:]):
        #         if temp > originalTemp:
        #             result[-1] = index + 1
        #             break
        # return result        
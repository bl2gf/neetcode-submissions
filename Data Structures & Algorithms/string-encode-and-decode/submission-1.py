class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedFinalString =""
        for i in range(len(strs)):
            encodedSubstring = str(len(strs[i])) + '#' + strs[i] 
            encodedFinalString +=encodedSubstring
        return encodedFinalString
    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decodedList.append(s[i:j])
            i = j 
        return decodedList
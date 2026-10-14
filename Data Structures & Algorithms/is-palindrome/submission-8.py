class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNoSpace = ""
        for c in s:
            if c.isalnum():
                sNoSpace+=c.lower()
        left = 0
        right = len(sNoSpace) -1
        while left <= right:
            if sNoSpace[left] != sNoSpace[right]:
                return False
            else:
                left+=1
                right -=1
        return True
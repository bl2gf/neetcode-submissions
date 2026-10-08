class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpecial = ''.join([char for char in s if char.isalnum()])
        print(noSpecial)
        reverse = noSpecial[::-1]
        return noSpecial.lower() == reverse.lower()
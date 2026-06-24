class Solution:
    def isPalindrome(self, s: str) -> bool:
        out=""
        for i in s:
            if i.isalnum():
                i=i.lower()
                out+=i
        if out == out[::-1]:
            return True
        else:
            return False
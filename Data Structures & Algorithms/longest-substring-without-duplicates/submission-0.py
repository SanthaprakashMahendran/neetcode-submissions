class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        unique=set()
        length=0
        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left=left+1
            unique.add(s[right])
            length=max(length, right-left+1)
            right=right+1
        return length


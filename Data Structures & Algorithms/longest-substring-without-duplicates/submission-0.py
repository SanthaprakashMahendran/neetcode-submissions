class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        unique=set()
        maxlen=0

        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[right])
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen

        ################
        # Using set to find duplicates
        # use while to remove until the duplicate is removed
        ################

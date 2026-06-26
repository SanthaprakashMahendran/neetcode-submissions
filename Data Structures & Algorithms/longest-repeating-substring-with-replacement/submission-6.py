class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        right=0

        maxfreq=0
        maxlen=0

        while right < len(s):
            count[s[right]]=1+count.get(s[right],0)
            maxfreq=max(maxfreq,count[s[right]])

            if (right-left+1 - maxfreq <= k):
                maxlen=max(maxlen,right-left+1)
            else:
                count[s[left]]=count.get(s[left])-1
                left=left+1
            right=right+1
        return maxlen




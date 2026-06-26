class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,0
        maxlen=0
        count={}
        maxFreq=0
        
        while right < len(s):
            count[s[right]]=1+count.get(s[right],0)
            maxFreq = max(maxFreq, count[s[right]])
            if (right-left+1 - maxFreq <= k):
                maxlen=max(maxlen,right-left+1)
            else:
                count[s[left]]=count.get(s[left])-1
                left+=1
            right+=1

        return maxlen
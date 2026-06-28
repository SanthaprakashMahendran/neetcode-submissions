class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,right=0,0
        countS,countT={},{}
        
        minLen=float('infinity')
        minString=[-1,-1]

        for i in t:
            countT[i]=1+countT.get(i,0)
        
        have,need=0,len(countT)

        while right < len(s):
            ch=s[right]
            countS[ch]=1+countS.get(ch,0)
            if ch in countT and countS.get(ch) == countT.get(ch):
                have+=1

            while have==need:
                if right-left+1<minLen:
                    minString=[left,right]   
                    minLen=right-left+1           

                countS[s[left]]=countS[s[left]]-1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have=have-1
                left+=1
            
            right+=1

        left,right=minString

        if minLen!=float('infinity'):
            return s[left:right+1]
        else:
            return ""




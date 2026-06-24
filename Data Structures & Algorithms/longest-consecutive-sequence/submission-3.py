class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        unique = sorted(set(nums))
        max_val=1
        for i in range(0, len(unique)):
            count=1
            for j in range(i+1,len(unique)):
                if unique[j]==unique[j-1]+1:
                    count+=1
                else:
                    break
                max_val=max(count,max_val)
        return max_val



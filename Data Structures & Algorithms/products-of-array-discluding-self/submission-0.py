class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(0,len(nums)):
            prod=1
            for j in range(0,len(nums)):
                if i == j:
                    continue
                else:
                    prod=prod*nums[j]
            out.append(prod)
        return out
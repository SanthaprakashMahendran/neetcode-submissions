class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val=set(nums)
        if len(nums) == len(list(val)):
            return False
        else:
            return True
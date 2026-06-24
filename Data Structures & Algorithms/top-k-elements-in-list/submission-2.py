from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        out=[]

        val=sorted(freq.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            out.append(val[i][0])
        return out

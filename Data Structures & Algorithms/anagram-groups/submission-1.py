class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for i in strs:
            val = "".join(sorted(i))
            if val not in out:
                out[val] = []
            out[val].append(i)
        return list(out.values())

        """"
        {
        act=[act,cat]
        pots=[post,tops,stop]
        hat=[hat]
        }
        """
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = []
        dg = {}
        for s in strs:
            key = "".join(sorted(s))
            dg[key] = dg.get(key,[])
            dg[key].append(s)
        return list(dg.values())
            
                


            
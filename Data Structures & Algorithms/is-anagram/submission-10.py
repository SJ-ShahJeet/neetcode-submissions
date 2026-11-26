class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i],0) + 1
            dt[t[i]] = dt.get(t[i],0) + 1
        if ds == dt :
            return True
        return False
"""           
        lt = list(t)
        for i in s:
            if i  not in lt:
                return False
            lt.remove(i)
                
        if len(lt) == 0:
            return True
        return False
"""
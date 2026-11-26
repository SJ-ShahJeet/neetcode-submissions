class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        maxl = 0

        for i in s:
            if i not in sub:
                sub += i
            else:
                j = sub.index(i)
                sub = sub[j+1:] + i
            maxl = max(maxl,len(sub))
        return maxl


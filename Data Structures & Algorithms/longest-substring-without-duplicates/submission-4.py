class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ml = 0
        temp = set()

        while r < len(s):

            while s[r] in temp:
                temp.remove(s[l])
                l += 1

            temp.add(s[r])
            ml = max(ml, r - l + 1)
            r += 1

        return ml
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        maxarea = 0
        while l <r :
            if heights[l] < heights[r] :
                area = (r-l) * heights[l]
                l += 1
            else :
                area = (r-l) * heights[r]
                r -= 1
            maxarea = max(maxarea,area)
        return maxarea
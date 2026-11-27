class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = [1]*len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            prd[i] = left
            left *=nums[i]
        for j in range(len(nums)-1,-1,-1):
            prd[j] *= right
            right *= nums[j]
        return prd


        

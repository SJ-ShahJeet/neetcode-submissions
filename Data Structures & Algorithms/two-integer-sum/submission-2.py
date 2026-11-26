class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        temp = []
        for i in range(len(nums)-1):
            diff = target - nums[i]
            temp = nums[i+1:]
            if diff in temp:
                return [i,temp.index(diff)+1+i]
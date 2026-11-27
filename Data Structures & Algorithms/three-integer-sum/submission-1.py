class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]

            while l < r:
                total = nums[l] + nums[r]

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return [list(t) for t in result]
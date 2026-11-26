class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq_bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in c.items():
            freq_bucket[freq].append(num)
        res = []
        for i in range(len(freq_bucket)-1,0,-1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

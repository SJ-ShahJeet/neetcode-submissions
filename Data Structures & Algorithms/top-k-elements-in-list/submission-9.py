class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dn = {}
        for n in nums:
            dn[n] = dn.get(n,0) + 1
        sdn = sorted(dn,key=dn.get,reverse=True)
        return sdn[:k]
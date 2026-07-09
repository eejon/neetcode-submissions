class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using hashmap can solve in O(n)
        # Using sort, can solve in O(n) possibly faster
        hset = set()
        for i in nums:
            if i in hset:
                return True
            hset.add(i)
        return False
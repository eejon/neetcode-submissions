class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in hmap:
                if i == hmap[target-nums[i]]:
                    continue
                return sorted([i, hmap[target-nums[i]]])
                
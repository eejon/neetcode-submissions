class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] = target
        # nums[i] = target - nums[j]
        # Bottleneck of an O(n^2) solution is comparing i and j -> nested for loop
        hmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hmap: 
                return [hmap[diff], i]
            hmap[nums[i]]=i
            
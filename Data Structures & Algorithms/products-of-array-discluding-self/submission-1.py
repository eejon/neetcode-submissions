class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        total = 1
        for i in range(len(nums)):
            ans.append(total)
            total *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
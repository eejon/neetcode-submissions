class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [2*4*6, 4*6, 6, 1] -> right
        # [1, 1, 1*2, 1*2*4] -> left
        # [-1, 0, 1, 2, 3]
        # [0*1*2*3, 1*2*3, 2*3, 3, 1] -> right
        # [1, -1, -1*0, -1*0*1, -1*0*1*2] -> left
        right = [1]*len(nums)
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = right[i]*nums[i]

        left = [1]*len(nums)
        for i in range(len(nums)-1):
            left[i+1] = left[i] * nums[i]

        return [ right[i]*left[i] for i in range(len(nums)) ]
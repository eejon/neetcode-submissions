class Solution:
    def trap(self, height: List[int]) -> int:
        # For each height, identify how much water it can hold
        # vol = min(height[l], height[r]) - height[i]

        # height[l] and height[r] needs to be the maximum boundaries
        # e.g. i = 2, 
        #   max height from left is height[1]=2
        #   max height from right is height[7]=3
        #   vol = min(2, 3) - 0 = 2
        # e.g. i = 4,
        #   max height from left is height[3]=3
        #   max height from right is height[7]=3
        #   vol = min(3, 3) - 1 = 2
        # e.g. i = 5, 
        #   max height from left is height[3]=3
        #   max height from right is height[7]=3
        #   vol = min(3, 3) - 0 = 3
        max_left = [0] * len(height)
        max_left[0] = height[0]
        for i in range(1, len(height)-1): max_left[i] = max(max_left[i-1], height[i])
        
        max_right = [0] * len(height)
        max_right[-1] = height[-1]
        for i in range(len(height)-2, -1, -1): max_right[i] = max(max_right[i+1], height[i])

        ans = 0
        for i in range(len(height)-1):
            if i == 0 or i == len(height)-1: continue
            # can only contain water if height[i] < left and height[i] < right
            left, right = max_left[i-1], max_right[i+1]
            if height[i] > left or height[i] > right: continue
            ans += min(left, right) - height[i]

        return ans
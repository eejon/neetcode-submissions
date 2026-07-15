class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Calculate volume:
        #   Choose any 2 heights, l and r
        #   Then, vol = height * width
        #   which is vol = min(heights[l], height[r]) * (r-l)

        # Maximize volume:
        #   After selecting a pair, compare their heights.
        #   Keep the taller, move the smaller.
        
        # Greedy search for solution, update largest

        l, r, ans = 0, len(heights)-1, 0
        while (l < r):
            vol = min(heights[l], heights[r]) * (r-l)
            # update greatest so far
            ans = max(ans, vol)
            if (heights[l] < heights[r]): l+=1
            else: r-=1
        return ans
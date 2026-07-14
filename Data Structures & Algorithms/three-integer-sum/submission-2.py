class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        # [-1, -1, -1, 0, 1, 2, 2]
        ans = []
        nums.sort()
        t = 0
        while (t < len(nums)-1):
            while t != 0 and t < len(nums)-1 and nums[t] == nums[t-1]: 
                t+=1
            l, r = t+1, len(nums)-1
            while (l < r):
                if nums[l] + nums[r] == -nums[t]:
                    ans.append([nums[t], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]: l+=1
                    while r > l and nums[r] == nums[r+1]: r-=1
                elif nums[l] + nums[r] > -nums[t]:
                    r-=1
                else:
                    l+=1
            t+=1
        return ans
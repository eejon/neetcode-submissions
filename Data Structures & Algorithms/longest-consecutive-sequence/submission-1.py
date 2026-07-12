class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Previous solution was not exactly right:
        # 1st bug: use pass instead of continue
        # 2nd bug: by trying to build the sequence with i+1, 
        #          worse case is O(n^2), e.g. [5,4,3,2,1] 
        # Improvement: build from start of sequence, not random point
        hset = set(nums)
        ans = 0
        for i in hset: # Iterate the hset instead to skip duplicates
            # check if SOS
            if i-1 not in hset:
                curr = 1
                while (i + curr) in hset:
                    curr+=1
                ans = max(curr, ans)
        return ans
                
                


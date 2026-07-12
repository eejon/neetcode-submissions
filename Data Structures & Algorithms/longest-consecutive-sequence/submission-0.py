class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use 2 sets:
        # exist: stores all elements in nums
        # seen: stores only explored elements in nums
        # longest variable to track
        # for i in nums:
        #     if i in seen: pass
        #     curr = 1
        #     seen.add(i)
        #     next = i+1
        #     while next in exist:
        #         seen.add(next)
        #         curr+=1
        #         next += 1
        #     longest = max(longest, next)
        # retun longest
        seen = set()
        exist = set()
        exist.update(nums)
        ans = 0
        for i in nums:
            if i in seen:
                pass
            curr = 1
            seen.add(i)
            next_ = i+1
            while next_ in exist:
                seen.add(next_)
                curr+=1
                next_+=1
            ans = max(curr, ans)
        return ans

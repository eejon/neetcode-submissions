class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window -> finding optimal window s.t.
        # window = all same character = best length
        # valid window => if can replace all characters
        l=r=0
        count = {}
        max_freq = 0
        res = 1
        while (r < len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            W=r-l+1
            if (W-max_freq > k):
                count[s[l]]-=1
                l+=1
            else: 
                res = max(W, res)
            r+=1
        return res
        
        
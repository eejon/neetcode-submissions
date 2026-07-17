class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        bp = sp = 0
        seen = {}
        for i,c in enumerate(s):
            if c in seen:
                bp = max(seen[c]+1, bp)
                sp = i
                seen[c] = i, seen[c]
            else:
                sp = i
            longest = max(longest, sp-bp+1)
            seen[c]=i
        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        # window must contain unique characters
        # windows length determined by number of unique characters
        # l=r=0
        # add s[r] to {} | if s[r] in {}, l=seen[s[r]]
        # r+=1
        l=r=0
        seen={}
        longest=0
        while (r < len(s)):
            if s[r] in seen:
                l=max(seen[s[r]]+1, l)
            seen[s[r]]=r
            longest=max(longest, r-l+1)
            r+=1
        return longest
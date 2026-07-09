class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = [0] * 26
        t_ = [0] * 26
        for c in s: s_[ord(c)-97]+=1
        for c in t: t_[ord(c)-97]+=1
        for i in range(26):
            if s_[i] != t_[i]: return False
        return True
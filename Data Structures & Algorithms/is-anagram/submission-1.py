class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort is O(n lg n)
        # hashmap would be O(n)
        if len(s) != len(t): return False
        hmap_s = {}
        hmap_t = {}
        for c in s:
            hmap_s[c] = hmap_s.get(c, 0) + 1
        for c in t:
            hmap_t[c] = hmap_t.get(c, 0) + 1
        
        for k in hmap_s:
            if hmap_t.get(k) != hmap_s[k]:
                return False
        return True
        
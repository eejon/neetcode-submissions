class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for s in strs:
            countArr = [0] * 26
            for c in s:
                countArr[ord(c)-ord('a')]+=1
            hmap[tuple(countArr)].append(s)

        return list(hmap.values())

class Solution:

    def _header(self, s: str) -> str:
        return f"[{len(s):03}]"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=self._header(s)
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            if s[i] == '[' and s[i+4] == ']': # is length header
                length = int(s[i+1:i+4])
                res.append(s[i+5:i+5+length])
                i+=5+length
        return res
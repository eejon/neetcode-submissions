class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = 0;
        int bp = 0, sp = 0;
        std::unordered_map<int, int> seen;
        for (size_t i=0; i<s.length(); ++i) {
            sp = i; // update stack pointer
            // seen before: move bp
            if (seen.contains(s[i])) {
                // update the bp
                bp = (bp > seen[s[i]]+1) ? bp : seen[s[i]]+1;
            }
            // update seen regardless
            seen[s[i]]=i;
            // calculate len
            int l = sp-bp+1;
            len = (l > len) ? l : len;
        }
        return len;
    }
};

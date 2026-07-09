class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<vector<string>> ans;
        std::unordered_map<string, std::vector<string>> groups;
        // iterate words
        for (const string& s : strs) {
            // create charCounter
            int charCounter[26] = {0};
            // fill up charCounter
            for (const char& c : s) {
                charCounter[c-'a']++;
            }
            // convert charCounter into hashable string
            string representative (26, 0);
            for (int i=0; i<std::size(charCounter); ++i) {
                representative[i]=static_cast<char>(charCounter[i]);
            }
            // Add to groups
            groups[representative].push_back(s);
        }
        // Update answer with groups
        for (const auto& [key, val] : groups) {
            ans.push_back(val);
        }
        return ans;
    }
};

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        std::vector<vector<string>> ans;
        std::unordered_map<string, std::vector<string>> groups;
        // iterate words
        for (const string& s : strs) {
            // create charCounter
            string charCounter (26, 0);
            // fill up charCounter
            for (const char& c : s) {
                charCounter[c-'a']++;
            }
            // Add to groups
            groups[charCounter].push_back(s);
        }
        // Update answer with groups
        for (const auto& [key, val] : groups) {
            ans.push_back(val);
        }
        return ans;
    }
};

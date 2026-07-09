class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<vector<string>> ans;
        std::unordered_map<string, std::vector<string>> groups;

        for (const string& s : strs) {
            string charCounter (26, 0);
            for (const char& c : s) {
                charCounter[c-'a']++;
            }

            groups[charCounter].push_back(s);
        }

        for (const auto& [key, val] : groups) {
            ans.push_back(val);
        }

        return ans;
    }
};

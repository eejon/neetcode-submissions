class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        std::sort(nums.begin(), nums.end());
        // Iterate through nums, selecting target
        for (int t=0; t<nums.size()-1; t++) {
            int target = nums[t];
            // If the target is already greater than 0, we can exit
            if (target > 0) break;
            // Skip duplicate targets (if seen before)
            if (t != 0 && nums[t-1] == target) continue;
            // Set up left and right pointers
            int l = t+1, r = nums.size()-1;
            while (l < r) {
                int sum = nums[l] + nums[r];
                // If sum is < -target move the left pointer
                if (sum < -target) l++;
                // If sum is > -target move the right pointer
                if (sum > -target) r--;
                // If a solution is found
                if (sum == -target) {
                    res.push_back({target, nums[l], nums[r]}); // add solution
                    // Start new position for both pointers
                    l++; r--;
                    // skip duplicates 
                    while (l<r && nums[l-1] == nums[l]) l++;
                }
            }
        }
        return res;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size()-1;
        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (target == sum) break;
            if (sum > target) r--;
            else l++;
        }
        return {l+1, r+1};
    }
};

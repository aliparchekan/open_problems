class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result;
        if(nums.size() == 0) {
            result.push_back(0);
            return result;
        }
        result.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++){
            result.push_back(result[i - 1] + nums[i]);
        }
        return result;
    }
};
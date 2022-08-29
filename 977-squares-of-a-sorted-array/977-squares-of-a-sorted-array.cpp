class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int begin = 0, end = nums.size() - 1;
        vector<int> result;
        while(begin <= end){
            if (abs(nums[begin]) > abs(nums[end])){
                result.insert(result.begin(), nums[begin] * nums[begin]);
                begin += 1;
            } else {
                result.insert(result.begin(), nums[end] * nums[end]);
                end -= 1;
            }
        }
        return result;
    }
};
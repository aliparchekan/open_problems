#include <algorithm>
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int begin = 0, end = nums.size() - 1;
        vector<int> result;
        while(begin <= end){
            if (abs(nums[begin]) > abs(nums[end])){
                result.push_back(nums[begin] * nums[begin]);
                begin += 1;
            } else {
                result.push_back(nums[end] * nums[end]);
                end -= 1;
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
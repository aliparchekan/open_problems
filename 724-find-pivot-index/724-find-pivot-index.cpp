class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        int n = 0;
        for (int i = 0; i < nums.size(); i++) total += nums[i];
        for (int i = 0; i < nums.size(); i++){
            if(n == total - n - nums[i]) return i;
            n += nums[i];
        }
        return -1;
    }
};
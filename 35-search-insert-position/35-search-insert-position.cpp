class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if(nums.size() == 0) return 0;
        int begin = 0, end = nums.size() - 1;
        int middle = begin + (end - begin) /2 ;
        while(begin <= end) {
            if(nums[middle] == target) return middle;
            if(nums[middle] < target) {
                begin = middle + 1;
            } else {
                end = middle - 1;
            }
            middle = begin + (end - begin) / 2;
            
        }
        return end + 1;
    }
};

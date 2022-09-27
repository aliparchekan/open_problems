class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int location = 0;
        int previous = -1000;
        for (int i = 0; i < nums.size(); i++){
            if (previous == nums[i]){
                continue;
            }
            nums[location] = nums[i];
            location ++;
            previous = nums[i];
        }
        return location++;
    }
};
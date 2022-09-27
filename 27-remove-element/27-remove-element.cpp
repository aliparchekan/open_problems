class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int location = 0;
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] == val){
                continue;
            } else {
                nums[location] = nums[i];
                location++;
            }
        }
        return location++;
    }
};
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // for(int i = 0; i < nums.size(); i++) {
        //     cout << nums[i] << ' ';
        // }
        // cout << endl;
        if(nums.size() == 0) return -1;
        if(nums.size() == 1){
            if (nums[0] == target) return 0;
            return -1;
        }
        int middle = nums.size() / 2;
        // cout << "middle is" << middle << endl;
        if(target == nums[middle]) return middle;
        if (target < nums[middle]) 
        {
            vector<int> new_vec = vector<int>(nums.begin(), nums.begin() + middle);
            int result = search(new_vec, target);
            if(result == -1) return -1;
            return result;
        }
        vector<int> new_vec = vector<int>(nums.begin() + middle, nums.end());
        int result = search(new_vec, target);
        if (result == -1) return -1;
        return  result + middle;
    }
};
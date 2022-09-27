class Solution {
public:
    int lengthOfLastWord(string s) {
        int flag = 0;
        int counter = 0;
        for(int i = s.size() - 1; i >= 0; i--){
            if (flag == 0 and s[i] == ' ') continue;
            else if(s[i] == ' ') return counter;
            flag = 1;
            counter++;
        }
        return counter;
    }
};
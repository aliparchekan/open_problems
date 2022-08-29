#include <string>
class Solution {
public:
    bool isSubsequence(string s, string t) {
        size_t position = 0;
        for(int i = 0; i< s.size(); ++i) {
            size_t n = t.find(s[i], position);
            if (n == string::npos) return false;
            position = n + 1;
        }
        return true;
    }
};
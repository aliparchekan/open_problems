class Solution {
public:
    bool isValid(string s) {
        map<char, char> matching = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        stack<char> values;
        for(int i = 0; i < s.size(); i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                values.push(s[i]);
            } else {
                if(values.empty()) return false;
                if (matching[values.top()] == s[i]) {
                    values.pop();
                } else {
                    return false;
                }
            }
        }
        return values.empty();
    }
};
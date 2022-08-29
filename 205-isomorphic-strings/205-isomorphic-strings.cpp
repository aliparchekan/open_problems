#include <map>
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> table;
        set<char> values;
        for(int i=0; i< s.size(); ++i){
            table[s[i]] = t[i];
            values.insert(t[i]);
        }
        if (values.size() != table.size()) return false;
        string new_string= "";
        for(int i = 0; i < s.size(); ++i){
            new_string += table[s[i]];
        }
        if(new_string == t) return true;
        return false;
    }
};
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int checkInterval(int n1, int n2) {
        if(isBadVersion(n1) && isBadVersion(n2)) return n1;
        uint middle = n1+ (n2 - n1) / 2;
        if(isBadVersion(middle)) {
            return checkInterval(n1, middle);
        }
        return checkInterval(middle + 1, n2);
    }
    int firstBadVersion(int n) {
        return checkInterval(1, n);
    }
};
// title: Pow(x, n)
// timestamp: 2024-02-22 07:51:36
// problemUrl: https://leetcode.com/problems/powx-n/
// memory: 8.2 MB
// runtime: 0 ms

// #include <cmath>

class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            long long m = n;
            return pow(1/x, -m);
        }
        return pow(x, n);
    }
    double pow(double x, long long n) {
        if (n == 1) {
            return x;
        }
        if (n % 2 == 0) {
            return pow(x * x, n / 2);
        } else {
            return x * pow(x * x, n / 2);
        }
    }
};
#include <algorithm>
#include <climits>
using namespace std;

int downStairs(int T[], unsigned int n) {
    if (n == 0) return 0;
    
    int dp[52];
    dp[0] = 0; // Start
    dp[1] = T[0];
    
    for (unsigned int i = 2; i <= n; i++) {
        dp[i] = max(dp[i-1], dp[i-2]) + T[i-1];
    }
    
    return max(dp[n], n >= 2 ? dp[n-1] : 0);
}
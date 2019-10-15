//#include <stdio.h>
//
//long long dp[91] = { 0, };
//
//long long f(int n) {
//	if (n == 0) return 0;
//	if (dp[n] != 0) {
//		return dp[n];
//	}
//	else {
//		dp[n] = f(n - 1) + f(n - 2);
//		return dp[n];
//	}
//}
//
//
//int main_() {
//	int N;
//	scanf("%d", &N);
//	dp[1] = 1;
//	printf("%lld\n", f(N));
//	return 0;
//}
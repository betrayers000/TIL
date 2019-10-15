//#include <stdio.h>
//
//int dp[1000001] = { 0, };
//
//int get_min(int n, int m) {
//	if (n == 0) return m;
//	else {
//		if (n > m) return m;
//		else return n;
//	}
//}
//
//int main_() {
//	int N;
//	scanf("%d", &N);
//	int i = 1;
//	while (i < N) {
//		if (i * 3 <= 1000000) {
//			dp[i * 3] = get_min(dp[i * 3], dp[i] + 1);
//		}
//		if (i * 2 <= 1000000){
//		dp[i * 2] = get_min(dp[i * 2], dp[i] + 1);
//		}
//		if (i + 1 <= 1000000) {
//			dp[i + 1] = get_min(dp[i + 1], dp[i] + 1);
//		}
//		i += 1;
//	}
//	printf("%d", dp[N]);
//	return 0;
//}
#include <stdio.h>

int dp[12] = {0,};

int f(int n) {
	if (n == 0) return 0;
	if (n == 1) return 1;
	if (n == 2) return 2;
	if (n == 3) return 4;
	if (dp[n] != 0) {
		return dp[n];
	}
	else {
		dp[n] = f(n - 1) + f(n - 2) + f(n-3);
		return dp[n];
	}
}

int main() {
	int T, N;
	scanf("%d", &T);
	dp[2] = 1;
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		printf("%d\n", f(N));
	}
	return 0;
}
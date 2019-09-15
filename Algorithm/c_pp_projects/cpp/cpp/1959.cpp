#include <stdio.h>

int check(int arr1[], int arr2[], int s, int l) {
	int set = l - s;
	int maxV = 0;
	for (int start = 0; start <= set; start++) {
		int total = 0;
		for (int i = start; i < l; i++) {
			total += arr1[i - start] * arr2[i];
		}
		if (total > maxV) {
			maxV = total;
		}
	}
	return maxV;
}


int main() {
	int T;
	scanf("%d", &T);	
	for (int tc = 1; tc <= T; tc++) {
		int N, M;
		scanf("%d", &N);
		scanf("%d", &M);
		int arr_N[20] = { 0, };
		int arr_M[20] = { 0, };
		int input;
		for (int i = 0; i < N; i++) {
			scanf("%d", &input);
			arr_N[i] = input;
		}
		for (int i = 0; i < M; i++) {
			scanf("%d", &input);
			arr_M[i] = input;
		}
		int result;
		if (N > M) {
			result = check(arr_M, arr_N, M, N);
		}
		else {
			result = check(arr_N, arr_M, N, M);
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}
#include <stdio.h>

int mabs(int n, int m) {
	if (n > m) {
		return n - m;
	}
	else {
		return m - n;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, arr[20];
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
		}
		int minV = 99999;
		int temp_abs, temp_index;
		for (int i = 0; i < N; i++) {
			int left = 0;
			int right = 0;
			for (int j = 0; j <= i; j++) {
				left += arr[j];
			}
			for (int k = i + 1; k < N; k++) {
				right += arr[k];
			}
			temp_abs = mabs(left, right);
			printf("%d ", temp_abs);
			if (minV > temp_abs) {
				minV = temp_abs;
				temp_index = i;
			}

		}
		printf("%d\n", temp_index);

	}
	return 0;
}
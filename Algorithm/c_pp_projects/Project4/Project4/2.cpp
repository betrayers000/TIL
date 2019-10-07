#include <stdio.h>

int get_carrot(int n, int m) {
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
		int N, W, arr[20], temp, now;
		scanf("%d", &N);
		scanf("%d", &W);
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
		}
		int i = 0;
		int total_length = 0;
		now = W;
		while (i < N) {
			if (now >= arr[i]) {
				now -= arr[i];
				i += 1;
			}
			else {
				temp = arr[i] - now;
				arr[i] = temp;
				now = 0;
			}
			if (now == 0) {
				total_length += (i + 1) * 2;
				now = W;
			}
		}
		if (total_length == 0) {
			total_length = N * 2;
		}
		printf("%d\n", total_length);
	}
	return 0;
}
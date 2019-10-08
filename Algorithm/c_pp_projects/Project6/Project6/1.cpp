#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int arr[49][49], N, center, start, end;
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%1d", &arr[i][j]);
			}
		}
		center = N / 2;
		start = center;
		end = center;
		int total = 0;
		for (int i = 0; i < N; i++) {
			for (int j = start; j <= end; j++) {
				total += arr[i][j];
			}
			if (i > center) {
				start += 1;
				end -= 1;
			}
			else {
				start -= 1;
				end += 1;
			}
		}
		printf("%d", total);
	}
	return 0;
}
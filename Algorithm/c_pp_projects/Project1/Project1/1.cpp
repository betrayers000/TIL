#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, M, maxV;
		scanf("%d", &N);
		scanf("%d", &M);
		int arr[15][15];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &arr[i][j]);
			}
		}
		maxV = 0;
		int total;
		for (int x = 0; x <= N - M; x++) {
			for (int y = 0; y <= N - M; y++) {
				total = 0;
				for (int i = 0; i < M; i++) {
					for (int j = 0; j < M; j++) {
						total += arr[i+x][j+y];
						//printf("%d ", arr[i+x][j+y]);
					}
				}
				//printf("%d\n", total);
				if (maxV < total) {
					maxV = total;
				}
			}
		}

		printf("#%d %d\n", tc, maxV);
	}

	return 0;
}
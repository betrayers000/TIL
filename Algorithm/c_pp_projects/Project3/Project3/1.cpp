#include <stdio.h>

bool check(int n) {
	int k, temp;
	int i = 0;
	int ori = n;
	while (true) {
		k = ori % 10;
		if (i >= 1) {
			if (k > temp) {
				return false;
			}
		}
		temp = k;
		//printf("%d, %d\n", ori, k);
		if (ori - k == 0) {
			break;
		}
		ori = (ori - k) / 10;
		i += 1;
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, arr[30000];
		scanf("%d", &N);
		int maxV = -1;
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
			if (i != 0) {
				for (int j = 0; j < i; j++) {
					int temp = arr[j] * arr[i];
					if (check(temp)) {
						if (maxV < temp) {
							maxV = temp;
						}
					}
				}
			}
		}
		printf("#%d %d\n", tc, maxV);

	}
	return 0;
}
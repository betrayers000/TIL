#include <stdio.h>

int arr[100];

int max() {
	int maxV = 0;
	int res = 0;
	for (int i = 0; i < 100; i++) {
		if (arr[i] > maxV) {
			maxV = arr[i];
			res = i;
		}
	}
	return res;
}

int min() {
	int minV = 1000;
	int res = 0;
	for (int i = 0; i < 100; i++) {
		if (arr[i] < minV) {
			minV = arr[i];
			res = i;
		}
	}
	return res;
}

int main() {
	for (int tc = 1; tc <= 10; tc++) {
		int N;
		scanf("%d", &N);
		for (int i = 0; i < 100; i++) {
			scanf("%d", &arr[i]);
		}
		int s = 0;
		while (s < N) {
			int mxi = max();
			int mii = min();
			arr[mxi] -= 1;
			arr[mii] += 1;
			s += 1;
		}
		int res = arr[max()] - arr[min()];
		printf("%d\n", res);
	}
	return 0;
}
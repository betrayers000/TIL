#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int tc; tc <= T; tc++) {
		int N, total;
		scanf("%d", &N);
		total = 0;
		for (int n = 1; n <= N; n++) {
			if (n % 2 == 0) {
				total -= n;
			}
			else {
				total += n;
			}
		}
		printf("%d\n", total);
	}
	return 0;
}
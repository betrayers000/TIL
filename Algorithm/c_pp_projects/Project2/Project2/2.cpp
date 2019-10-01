#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, P;
		int term[5001] = { 0, };
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			int a, b;
			scanf("%d", &a);
			scanf("%d", &b);
			while (a <= b) {
				term[a] += 1;
				a += 1;
			}
		}
		scanf("%d", &P);
		printf("#%d", tc);
		for (int i = 0; i < P; i++) {
			int t;
			scanf("%d", &t);
			printf(" %d", term[t]);
		}
		printf("\n");
	}
	return 0;
}
#include <stdio.h>


int main() {

	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int a, b, div, mod;
		scanf("%d", &a);
		scanf("%d", &b);
		div = a / b;
		mod = a - (div*b);
		printf("#%tc %d %d", tc, div, mod);
	}
}
#include <stdio.h>

int main() {
	int T;
	char z;
	scanf("%d", &T);
	scanf("%c", &z);
	for (int tc = 1; tc <= T; tc++) {
		char arr[31], input;
		int k;
		int maxV;
		for (int i = 0; i < 31; i++) {
			scanf("%c", &input);
			arr[i] = input;
			if (i == 0) {
				k = 0;
			}
			else {
				printf("%c", input);
				if (arr[k] == input) {
					k += 1;
				}
				else {
					maxV = k;
					k = 0;
				}
			}
		}
		printf("%d\n", maxV);

	}
	return 0;
}
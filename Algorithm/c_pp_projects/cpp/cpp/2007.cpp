#include <stdio.h>

int main() {
	int T;
	char z;
	scanf("%d", &T);
	scanf("%d", &z);
	for (int tc = 1; tc <= T; tc++) {
		char arr[31];
		int cnt = 0;
		for (int i = 0; i < 31; i++) {
			char a = ' ';
			scanf("%1c", &a);
			arr[i] = a;
			printf("%c", arr[i]);
		}
		int k = 1;
		for (int i = 0; i < 31; i++) {

		}
	}
	return 0;
}
#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		char arr[20];
		char s;
		int cnt = 0;
		for (int i = 0; i < 20; i++) {
			scanf("%1c", &s);
			arr[i] = s;
			if (s == '\n') {
				break;
			}
			printf("%c", arr[i]);
			cnt += 1;
		}
		bool check = false;
		for (int i = 0; i < cnt - 1; i++) {
			if (check) {
				break;
			}
			if (arr[cnt -2- i] != arr[i]) {
				check = true;
			}
		}
		int result = 0;
		if (check) {
			result = 1;
		}
		printf("%d", result);
	}
	return 0;
}
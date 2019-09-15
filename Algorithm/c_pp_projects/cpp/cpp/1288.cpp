#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int arr[10] = { 0, };
		int input;
		scanf("%d", &input);
		int N = input;
		int k = 1;
		int cnt = 0;
		while (true) {
			int temp = N * k;
			if (cnt == 10) {
				break;
			}
			int num = temp;
			for (int i = 0; i < 7; i++) {
				if (num == 0) {
					break;
				}
				if (arr[num % 10] == 0) {
					arr[num % 10] = 1;
					cnt += 1;
				}
				num = num / 10;
			}
			k = k + 1;
		}
		printf("#%d %d\n", tc, (k - 1)*N);
	}
}
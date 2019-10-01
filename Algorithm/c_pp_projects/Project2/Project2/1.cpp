#include <stdio.h>

int count(int arr[]) {
	int cnt = 0;
	for (int i = 0; i < 13; i++) {
		//printf(" %d", arr[i]);
		if (arr[i] == 1) {
			cnt += 1;
		}
	}
	return 13 - cnt;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		char arr[3001];
		int arr_s[13] = { 0, };
		int arr_d[13] = { 0, };
		int arr_h[13] = { 0, };
		int arr_c[13] = { 0, };
		scanf("%s", arr);
		int num, a, b;
		bool check = true;
		int i = 0;
		while (arr[i] != '\0') {
			if (check == false) {
				break;
			}
			a = arr[i + 1] - '0';
			b = arr[i + 2] - '0';
			num = a * 10 + b -1;
			//printf("%d ", num);
			if (arr[i] == 'S') {
				if (arr_s[num] == 1) {
					check = false;
				}
				else {
					arr_s[num] = 1;
				}
			}
			else if (arr[i] == 'H') {
				if (arr_h[num] == 1) {
					check = false;
				}
				else {
					arr_h[num] = 1;
				}

			}
			else if (arr[i] == 'D') {
				if (arr_d[num] == 1) {
					check = false;
				}
				else {
					arr_d[num] = 1;
				}

			}
			else if (arr[i] == 'C') {
				if (arr_c[num] == 1) {
					check = false;
				}
				else {
					arr_c[num] = 1;
				}
			}
			i += 3;
		}
		if (check) {
			printf("#%d %d", tc, count(arr_s));
			printf(" %d", count(arr_d));
			printf(" %d", count(arr_h));
			printf(" %d\n", count(arr_c));
		}
		else {
			printf("#%d ERROR\n", tc);
		}

	}
	return 0;
}
#include <stdio.h>

int main() {
	int arr[4];
	int total = 0;
	int num;
	for (int i = 0; i < 4; i++) {
		scanf("%1d", &num);
		arr[i] = num;
		if (arr[i] > 0) {
			total += arr[i];
		}
	}
	printf("%d", total);
	return 0;
}
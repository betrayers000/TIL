#include <stdio.h>

int main() {
	int a, b, c, result;
	int arr[10] = { 0, };
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	result = a * b * c;
	//printf("%d", result);
	while (result != 0) {
		int temp = result % 10;
		result = (result - temp) / 10;
		arr[temp] += 1;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}
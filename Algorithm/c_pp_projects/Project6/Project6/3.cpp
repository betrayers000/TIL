#include <stdio.h>

int main() {
	char arr[100];
	int alv[26] = { 0, };
	scanf("%s", arr);
	int i = 0;
	while (arr[i] != '\0') {
		int idx = arr[i] - 97;
		if (alv[idx] == 0) {
			alv[idx] = i + 1;
		}
		i += 1;
	}
	for (int i = 0; i < 26; i++) {
		printf("%d ", alv[i] - 1);
	}
	printf("\n");
	return 0;
}
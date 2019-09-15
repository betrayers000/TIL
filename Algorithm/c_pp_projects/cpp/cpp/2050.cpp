#include <stdio.h>
#include <string>

using namespace std;

int search_char(char str) {
	char upper_arr[] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
	char lower_arr[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
	for (int i = 0; i < 26; i++) {
		if (str == upper_arr[i]) {
			return i + 1;
		}
		if (str == lower_arr[i]) {
			return i + 1;
		}
	}
	return 0;
}

int main() {
	char arr[200];
	string word;
	scanf("%s", &arr);
	word = arr;
	for (int i = 0; i < word.size(); i++) {
		printf("%d ", search_char(arr[i]));
	}
	return 0;
}
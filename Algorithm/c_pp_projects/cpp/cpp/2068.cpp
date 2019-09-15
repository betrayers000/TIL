#include <stdio.h>

int change(int arr[], int i, int j)
{
	for (int k = 1; k <= i - j; k++)
	{
		int temp = 0;
		temp = arr[i - k];
		arr[i - k + 1] = temp;
	}
	return 0;
}

int main()
{
	int N, div;
	scanf("%d", &N);
	int arr[199];
	div = (N - 1) / 2;
	for (int i = 0; i < N; i++)
	{
		arr[i] = -1;
		int num;
		scanf("%d", &num);
		for (int j = 0; j < N; j++)
		{
			if (arr[j] == -1)
			{
				arr[j] = num;
				break;
			}
			if (num <= arr[j])
			{
				change(arr, i, j);
				arr[j] = num;
				break;
			}
		}
	}
	printf("%d", arr[div]);

	return 0;
}
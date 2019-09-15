#include <stdio.h>

int change(int arr[], int i, int j)
{
    for (int k = 0; k <= j; k++)
    {
        int temp = 0;
        temp = arr[i - k - 1];
        arr[i - k] = temp;
    }
    return 0;
}

int main()
{
    printf("hellowword");
    int N, div;
    scanf("%d", &N);
    int arr[N];
    div = (N - 1) / 2;
    for (int i = 0; i < N; i++)
    {
        int num;
        scanf("%d", &num);
        for (int j = 0; j < N; j++)
        {
            if (arr[j] == 0)
            {
                arr[j] = num;
                break;
            }
            if (num < arr[j])
            {
                change(arr, i, j);
                arr[j] = num;
                break;
            }
        }
    }
    for (int i = 0; i < N; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("%d\n", arr[div]);
    return 0;
}
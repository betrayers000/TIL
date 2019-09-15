#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc < T; tc++)
    {
        int total = 0;
        int num;
        for (int i = 0; i < 10; i++)
        {
            scanf("%d", &num);
            if (num % 2 == 1)
            {
                total += num;
            }
        }
        printf("#%d %d\n", total);
    }
    return 0;
}
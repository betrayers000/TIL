#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++)
    {
        float total = 0;
        int num;
        for (int i = 0; i < 10; i++)
        {
            scanf("%d", &num);
            total += num;
        }

        printf("#%d %0.f\n", tc, total / 10);
    }
    return 0;
}
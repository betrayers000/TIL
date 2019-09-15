#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++)
    {
        int maxV = 0;
        int num;
        for (int i = 0; i < 10; i++)
        {
            scanf("%d", &num);
            if (maxV < num)
            {
                maxV = num;
            }
        }
        printf("#%d %d\n", tc, maxV);
    }
    return 0;
}
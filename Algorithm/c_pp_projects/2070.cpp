#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++)
    {
        int num1, num2;
        int result = 0;
        scanf("%d", &num1);
        scanf("%d", &num2);
        if (num1 == num2)
        {
            printf("#%d =\n", tc);
        }
        else if (num1 < num2)
        {
            printf("#%d <\n", tc);
        }
        else
        {
            printf("#%d >\n", tc);
        }
    }
    return 0;
}
// Online C compiler to run C program online
#include <stdio.h>

int main()
{
    int startnum;
    int endnum;
    int decrement;

jump:
    printf("\n Enter startnumber :");
    scanf("%d", &startnum);

    if ((startnum > endnum) && (startnum <= 100))
    {
        printf("\n Entered number is  = %d", startnum);
    }
    else
    {
        printf("\n Entered number is not valid please rewrite");
        goto jump;
    }

rejump:
    printf("\n Enter endnumber :");
    scanf("%d", &endnum);

    if ((endnum < startnum) && (endnum > 0))
    {
        printf("\n Entered number is  = %d", endnum);
    }
    else
    {
        printf("\n Entered number is not valid please rewrite");
        goto rejump;
    }

decr:
    printf("\n Enter decrement :");
    scanf("%d", &decrement);
    if (decrement <= 0)
    {
        goto decr;
    }

    if ((startnum <= 100) && (startnum >= endnum) && (endnum >= 0))
    {
    rede:
        if (startnum >= endnum)
        {
            startnum = startnum - decrement;
            printf("\n startnum = %d", startnum);
            goto rede;
        }
        else
        {
            printf("\n End of loop");
        }
    }
    else
    {
        printf("\n Entered numbers are not valid :");
    }

    return 0;
};
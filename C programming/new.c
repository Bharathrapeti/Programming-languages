#include<stdio.h>
int main()
{
    int x[10],even,odd;
    int i;
    for(i=0;i<10;i++)
    {
        scanf("%d",&x[i]);
    }
    for(i=0;i<10;i++)
    {
        if(x[i]%2==0)
        {
            x[i]=even;
        }
        else
        {
            printf("x[%d]  is odd \n",x[i]);
        }
    }
    return 0;
}
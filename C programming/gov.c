#include<stdio.h>
int main()
{
    int n, i, sum=0;

    printf("enter the size of the array:");
    scanf("%d",&n);
    int arr[n];
    printf("enter the elements of the array:\n");

    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i+=2)
    {
        sum=sum+arr[i];
    }
    printf("the sum of the array elements is %d",sum);
    return 0;
}
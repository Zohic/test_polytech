#include "functions.h"

int FindMin(int arr[], int len)
{

    int min = arr[0];
    for(int i=1;i<len;i++)
        if(arr[i]<min)
            min = arr[i];
    return min;
}

int FindMax(int arr[], int len)
{
    int max = arr[0];
    for(int i=1;i<len;i++)
        if(arr[i]>max)
            max = arr[i];
    return max;
}

int CountEnters(int arr[], int len, int tar)
{
    int count = 0;
    for(int i=0;i<len;i++)
        if(arr[i]==tar)
            count++;
    return count;
}

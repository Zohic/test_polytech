#include "functions.h"

int FindElement(int arr[], int len, int tar)
{
    for(int i=0;i<len;i++)
    {
        if(arr[i]==tar)
            return i;
    }
    return -1;
}

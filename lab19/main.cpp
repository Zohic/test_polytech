// Допишите программу, которая вычисляет расстояние Хэмминга бинарных представлений двух целых положительных чисел.

#include <iostream>

int hamming(int a, int b)
{
    bool bit1, bit2;
    int ham=0;
    for(int i=0;i<sizeof(int)*8;i++)
    {
        bit1 = a%2;
        bit2 = b%2;
        a/=2;
        b/=2;
        ham+= (bit1!=bit2);
    }
    return ham;
}


int main() {
    std::cout << hamming(7, 3) << std::endl;
    return 0;
}

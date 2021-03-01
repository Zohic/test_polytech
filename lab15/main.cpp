// Вывести представление целого десятичного числа N в системе счисления с основанием M. M и N вводятся пользователем с клавиатуры.
// Для примера посмотрите задачу 14

#include <iostream>
const int maxBase = 24;
const char symbols[14]{'A','B','C','D','E','F','G','H','I','J','K','L','M','N'};

int main() {

    int N, M;

    std::cout << "enter positive number: ";
    std::cin >> N;
    std::cout << std::endl;
    std::cout << "choose base from 2 to 24: ";
    std::cin >> M;


    int digit;
    char* output = new char[1];
    int size = 1;

    while(true)
    {
        digit = N%M;
        N/=M;

        if(digit<10)
            output[size-1] = (char)(48+digit);
        else
            output[size-1] = symbols[digit-10];

        if(N>0)
        {
            char* newOut = new char[size+1];
            for(int i=0;i<size;i++)
            {
                newOut[i] = output[i];
            }

            size+=1;
            delete[] output;
            output = newOut;
        }else
            break;

    }

    for(int i=size-1;i>=0;i--)
       std::cout<<output[i];

    return 0;
}

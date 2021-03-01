// Вывести представлени десятичного числа N в системе счисления с основанием M. M и N вводятся пользователем с клавиатуры.
// Для примера посмотрите задаче целогоу 14

#include <iostream>

int main() {

    int N, M;

    std::cout << "enter positive number: ";
    std::cin >> N;
    std::cout << std::endl;
    std::cout << "choose base from 2 to 9: ";
    std::cin >> M;


    int digit;
    int output=0;
    int mul = 1;

    while(N>0)
    {
        digit = N%M;
        N/=M;
        output+=mul*digit;
        mul*=10;
    }
    std::cout<<output;

    return 0;
}

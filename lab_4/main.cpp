#include <iostream>
#include <string>


void GetDigits1(int num)
{
    for(int i=5;i>0;i--)
    {
        int p = std::pow(10,i);
        int p2 = std::pow(10,i-1);
        std::cout << floorf((num%p)/p2) << std::endl;
    }
}

void GetDigits2(int num)
{
    int pows[5] = {1,10,100,1000,10000};
    for(int i=5;i>0;i--)
    {
        int p = pows[i];
        int p2 = pows[i-1];
        std::cout << floorf((num%p)/p2) << std::endl;
    }
}

void GetDigits3(int num)
{
    std::string str = std::to_string(num);
    for(int i=0;i<str.size();i++)
    {
        std::cout << str[i] << std::endl;
    }
}

int main() {
    int inp;
    std::cin >> inp;

    GetDigits1(inp);
    GetDigits2(inp);
    GetDigits3(inp);

    return 0;
}

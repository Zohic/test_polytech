// Напишите функцию, которая заполняет массив случайными
// целыми числами из диапазона от 0 до n. Воспользуйтесь функциями
// std::rand() и std::srand().

#include <cstdlib>
#include <iostream>

void RandomFill(int arr[], int len, int n)
{
    for(int i=0;i<len;i++)
    {
        arr[i]=std::rand()%(n+1);
    }

}
const short int NUMS_LEN=30;
int main()
{
    //Прошу ввести случайное число для генерации более случайной последовательности
    int seed;
    std::cout<<"write random number please: ";
    std::cin >> seed;
    std::srand(seed*NUMS_LEN);

    int nums[NUMS_LEN];
    RandomFill(nums, NUMS_LEN, 100);

    for(int i=0;i<NUMS_LEN;i++)
        std::cout<<nums[i]<<std::endl;

    return 0;
}

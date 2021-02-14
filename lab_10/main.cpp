#include <iostream>

float absolute_value(float x)
{
   int b = *((int*)&x)&~(1<<31);
   return *((float*)&b);   
}

int main()
{
  std::cout << absolute_value(-2.717f) << std::endl;
  std::cout << absolute_value(3.1415f) << std::endl;
  return 0;
}

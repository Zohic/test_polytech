#include <iostream>

float absolute_value(float x)
{
   int b = *((int*)&x)&~(1<<31);
   return *((float*)&b);   
}

float absolute_value2(float x)
{
   if(x>=0)
      return x;
   else
      return -x;
}

float absolute_value3(float x)
{
   return x?x>=0:-x;
}


int main()
{
  std::cout << absolute_value(-2.717f) << std::endl;
  std::cout << absolute_value(3.1415f) << std::endl;
  return 0;
}

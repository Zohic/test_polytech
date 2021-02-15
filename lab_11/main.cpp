int GetMaxInt1()
{
    unsigned int prevInt = 0;
    unsigned int curInt = 1;
    while(prevInt==curInt/2)
    {
        prevInt=curInt;
        curInt*=2;
        //std::cout << curInt << std::endl;
    }
    return prevInt-1;
}

int GetMaxInt2()
{
    int prevInt = 0;
    int curInt = 1;
    while(prevInt==curInt/2)
    {
        prevInt=curInt;
        curInt*=2;
        //std::cout << curInt << std::endl;
    }
    return (prevInt-1)*2+1;
}

int GetMaxInt3()
{
    int integ = 0;
    return ((unsigned int)(~(integ)))>>1;
}

int GetMaxInt4()
{
    unsigned int integ = 0;
    return ~integ/2;
}


int main() {


    std::cout << GetMaxInt1() << std::endl;
    std::cout << GetMaxInt2() << std::endl;
    std::cout << GetMaxInt3() << std::endl;
    std::cout << GetMaxInt4() << std::endl;



    return 0;
}

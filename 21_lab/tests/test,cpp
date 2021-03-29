#include "functions.h"
#include "gtest/gtest.h"

//Test Find Max--------------------------------------------------------------------------------------------------------
TEST(testFindMax, firstOneMax)
{
    int arr[]={20,3,4,5};
    EXPECT_EQ(FindMax(arr, 4), 20);
}

TEST(testFindMax, lastOneMax)
{
    int arr[]={20,3,4,5,33};
    EXPECT_EQ(FindMax(arr, 5), 33);
}

TEST(testFindMax, nonFullSearch)
{
    int arr[]={-1,3,12,5,33,44,55};
    EXPECT_EQ(FindMax(arr, 4), 12);
}

TEST(testFindMax, SimpleTest)
{
    int arr[]={1,2,343,108,-108,0,12};
    EXPECT_EQ(FindMax(arr, 7), 343);
}
//Test Find Min--------------------------------------------------------------------------------------------------------
TEST(testFindMin, firstOneMin)
{
    int arr[]={-16,11,12,50,-10};
    EXPECT_EQ(FindMin(arr, 5), -16);
}

TEST(testFindMin, lastOneMin)
{
    int arr[]={1,32,4,5,0};
    EXPECT_EQ(FindMin(arr, 5), 0);
}

TEST(testFindMin, nonFullSearch)
{
    int arr[]={-1,-3,-13,0,-33,-44,-55};
    EXPECT_EQ(FindMin(arr, 4), -13);
}

TEST(testFindMin, SimpleTest)
{
    int arr[]={3,4,-10,0,1000,0,-11};
    EXPECT_EQ(FindMin(arr, 7), -11);
}
//Test Count Enters----------------------------------------------------------------------------------------------------
TEST(testCountEnters, sameNumbers)
{
    int arr[]={6,6,6,6,6,6};
    EXPECT_EQ(CountEnters(arr, 6, 6), 6);
}

TEST(testCountEnters, noEnters)
{
    int arr[]={1,2,3,4,5,6,7};
    EXPECT_EQ(CountEnters(arr, 7, 10), 0);
}

TEST(testCountEnters, nonFullSearch)
{
    int arr[]={1,20,3,40,5,7,7};
    EXPECT_EQ(CountEnters(arr, 5, 7), 0);
}

TEST(testCountEnters, SimpleTest)
{
    int arr[]={3,1,4,12,1,66,1,42,1};
    EXPECT_EQ(CountEnters(arr, 9, 1), 4);
}

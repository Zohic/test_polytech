#include "functions.h"
#include "gtest/gtest.h"

TEST(testSearch, firstOne)
{
    int arr[]={3, 2, 1, 2, 12, 34};
    EXPECT_EQ(FindElement(arr, 6, 3), 0);
}

TEST(testSearch, lastOne)
{
int arr[]={3, 2, 1, 2, 12, 34, 81};
EXPECT_EQ(FindElement(arr, 7, 81), 6);
}

TEST(testSearch, simpleTest)
{
int arr[]={12, 344, 652, 7, 123, 888, 352, 11, 88};
EXPECT_EQ(FindElement(arr, 9, 123), 4);
}

TEST(testSearch, noSuchElement)
{
int arr[]={12, 344, 652, 7, 123, 888, 352, 11, 88};
EXPECT_EQ(FindElement(arr, 9, 2021), -1);
}

TEST(testSearch, nonFullSearch)
{
int arr[]={1, 2, 3, 4, 22, 23, 25, 99};
EXPECT_EQ(FindElement(arr, 6, 25), -1);
}

#include <lnuRandom.h>

#include <FastStr.hpp>

// Zauważ, że nie używam danych 'FastStr', tylko jego interfejsu...
// To naprawdę powinien być obiekt, ale już trudno

TEST(ExTestForFastStr, InterfaceWorksAsExpected)
{
    FastStr str1;
    changeStr(str1, "hello");

    FastStr str2;
    changeStr(str2, "hello");

    ASSERT_TYPE_EQ(str1 == str2, bool);
}

TEST(ExTestForFastStr, CanDifferentiateStrings)
{
    FastStr str1;
    changeStr(str1, "hello");

    FastStr str2;
    changeStr(str2, "world");

    EXPECT_FALSE((str1 == str2));
}

TEST(ExTestForFastStr, CanBeUsedToFindEqualStrings)
{
    FastStr str1;
    changeStr(str1, "world");

    FastStr str2;
    changeStr(str2, "world");

    EXPECT_TRUE((str1 == str2));
}

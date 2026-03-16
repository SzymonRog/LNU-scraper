#include <lnuRandom.h>

#include <Vector2.hpp>

TEST(ExTestsForVector2, StructureContainsExpectedFields)
{
    // Wymagam, by były to double, bo są bardziej dokładne niż float
    ASSERT_TYPE_EQ(Vector2::x, double);
    ASSERT_TYPE_EQ(Vector2::y, double);
}

TEST(ExTestsForVector2, CanCreateUzingInitializerList)
{
    Vector2 vec{1.0, 2.0};

    EXPECT_EQ_MSG(vec.x, 1.0);
    EXPECT_EQ_MSG(vec.y, 2.0);
}

TEST(ExTestsForVector2, AdditionOfTwoVectors)
{
    Vector2 a{1.0, 2.0};
    Vector2 b{3.0, 4.0};
    auto res = a + b;

    ASSERT_TYPE_EQ(res, Vector2);

    EXPECT_EQ_MSG(res.x, 4.0);
    EXPECT_EQ_MSG(res.y, 6.0);
}

TEST(ExTestsForVector2, SubtractionOfTwoVectors)
{
    Vector2 a{1.0, 2.0};
    Vector2 b{3.0, 4.0};
    auto res = a - b;

    ASSERT_TYPE_EQ(res, Vector2);

    EXPECT_EQ_MSG(res.x, -2.0);
    EXPECT_EQ_MSG(res.y, -2.0);
}

TEST(ExTestsForVector2, MultiplicationOfVectorByScalar)
{
    Vector2 vec{1.0, 2.0};
    double n = 3.0;

    auto res1 = vec * n;
    auto res2 = n * vec;

    ASSERT_TYPE_EQ(res1, Vector2);
    ASSERT_TYPE_EQ(res2, Vector2);

    EXPECT_EQ_MSG(res1.x, 3.0);
    EXPECT_EQ_MSG(res1.y, 6.0);

    EXPECT_EQ_MSG(res2.x, 3.0);
    EXPECT_EQ_MSG(res2.y, 6.0);
}

TEST(ExTestsForVector2, DotProductOfTwoVectors)
{
    // pomiędzy wektorami jest kąt 90 stopni
    Vector2 vec1{2.0, 2.0};
    Vector2 vec2{-2.0, 2.0};
    auto res = vec1 * vec2;

    ASSERT_TYPE_EQ(res, double);

    EXPECT_EQ_MSG(res, 0.0);
}
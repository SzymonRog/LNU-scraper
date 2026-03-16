#include <Exhibit.hpp>
#include <Theme.hpp>
#include <app.cpp>

TEST(ExampleTestForCountDisplayed, WorksWithEmptyArray)
{
    Exhibit* exhibits;
    ASSERT_EQ(countDisplayed(exhibits, 0, Theme::ContemporaryArt), 0);
}

TEST(ExampleTestForCountDisplayed, WorksWithSmallArray)
{
    constexpr int arrSize = 3;
    const Exhibit* exhibits = new Exhibit[arrSize]{
        {"Sunrise", "France", Theme::Impressionism},
        {"Starry Night", "France", Theme::Impressionism, true},
        {"The Scream", "Norway", Theme::Expressionism}
    };

    EXPECT_EQ_MSG(countDisplayed(exhibits, arrSize, Theme::Impressionism), 1);
    delete[] exhibits;
}
#include <LnuTest.h>
#include <lnuRandom.h>

#include <vector>
#include <algorithm>

#include <Time.hpp>
#include <app.cpp>

TEST(itLives, itLives)
{
    ASSERT_TRUE(true);
}

TEST(TestIfTimeIsSortable, TestWithRandomValues)
{
    constexpr size_t n = 100;
    std::vector<Time> times(n);

    for(auto& time : times)
    {
        time.hour = lnu::getRandomInteger(0, 23);
        time.minute = lnu::getRandomInteger(0, 59);
    }

    // Funkcja std::sort używa '<' do porównywania elementów
    // Oczekuje ona również, że porównanie nie będzie modyfikować obiektów
    std::sort(times.begin(), times.end());

    // Specjalnie w ten sposób, żebyś nie zgapiał :)
    unsigned int h = 0;
    unsigned int m = 0;
    for(const auto& time : times)
    {
        ASSERT_TRUE((time.hour >= h));
        ASSERT_TRUE((time.minute + (time.hour-h)*60 >= m));
        h = time.hour;
        m = time.minute;
    }
}

TEST(TestIfTimeIsSortable, TestWithAllValuesInOneHour)
{
    constexpr size_t n = 100;
    std::vector<Time> times(n);

    for(auto& time : times)
    {
        time.hour = 1;
        time.minute = lnu::getRandomInteger(0, 59);
    }

    std::sort(times.begin(), times.end());

    unsigned int m = 0;
    for(const auto& time : times)
    {
        ASSERT_TRUE((time.minute >= m));
        m = time.minute;
    }
}

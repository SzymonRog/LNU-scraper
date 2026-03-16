/* Niestety nie mogę 'dobrze' i 'nieinwazyjnie' sprawdzić twojego zarządzania pamięcią,
 * bo nie mam wpływu na kształt Twoich struktur danych.
 * Musisz więc pilnować się sam :)
*/

#include <State.hpp>
#include <StateUtils.cpp>

TEST(TestState, UrlFieldIsString)
{
    ASSERT_TYPE_EQ(State::url, std::string);
}

TEST(TestState, NextFieldIsPointerToState)
{
    ASSERT_TYPE_EQ(State::next, State*);
}

TEST(TestState, PrevFieldIsPointerToState)
{
    ASSERT_TYPE_EQ(State::prev, State*);
}

TEST(ExTests, BasicCaseForNext)
{
    State s1;
    State s2;

    s1.next = &s2;

    ASSERT_FALSE(next(&s1, 1) == nullptr);
    EXPECT_EQ(next(&s1, 1), &s2);
}

TEST(ExTests, BasicCaseForPrev)
{
    State s1;
    State s2;

    s2.prev = &s1;

    ASSERT_FALSE(prev(&s2, 1) == nullptr);
    EXPECT_EQ(prev(&s2, 1), &s1);
}

TEST(ExTests, BasicCaseForAddNext)
{
    State s1;

    addNext(&s1, "http://www.example.com");
    
    ASSERT_FALSE(s1.next == nullptr);
    EXPECT_EQ(s1.next->url, "http://www.example.com");
}

TEST(ExTests, BasiCaseForInsert)
{
    State s1, s2;
    s1.next = &s2;
    s2.prev = &s1;
    
    insert(&s1, "http://www.example.com");
    
    ASSERT_FALSE(s1.next == nullptr);
    ASSERT_FALSE(s2.prev == nullptr);
    
    EXPECT_EQ(s1.next->url, "http://www.example.com");
    EXPECT_EQ(s2.prev->url, "http://www.example.com");
}
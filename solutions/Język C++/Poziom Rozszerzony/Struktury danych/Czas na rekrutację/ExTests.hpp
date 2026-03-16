#include <cmath>

#include <Node.hpp>
#include <app.cpp>

TEST(ExampleTestForFindMiddle, FunctionReturnsNullptrForEmptyList)
{
    EXPECT_EQ_MSG(findMiddle(nullptr), nullptr)
}

TEST(ExampleTestForFindMiddle, FunctionFindsMiddleWithOddNumberOfElements)
{
    constexpr int numberOfNodes = 3;
    Node* nodes = new Node[numberOfNodes];

    for(int i = 0; i < numberOfNodes-1; ++i)
    {
        nodes[i].data = i+1;
        nodes[i].next = &nodes[i + 1];
    }
    nodes[numberOfNodes-1].data = numberOfNodes;

    const Node* middle = findMiddle(nodes);
    EXPECT_EQ_MSG(middle->data, std::ceil(numberOfNodes/2.0))
    // std::ceil(numberOfNodes/2.0) = 2

    delete[] nodes;
}

TEST(ExampleTestForFindMiddle, FunctionFindsMiddleWithEvenNumberOfElements)
{
    constexpr int numberOfNodes = 4;
    Node* nodes = new Node[numberOfNodes];

    for(int i = 0; i < numberOfNodes-1; ++i)
    {
        nodes[i].data = i+1;
        nodes[i].next = &nodes[i + 1];
    }
    nodes[numberOfNodes-1].data = numberOfNodes;

    const Node* middle = findMiddle(nodes);
    EXPECT_EQ_MSG(middle->data, std::ceil(numberOfNodes/2.0))
    // std::ceil(numberOfNodes/2.0) = 2

    delete[] nodes;
}
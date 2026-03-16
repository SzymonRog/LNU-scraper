#include <Node.hpp>
#include <app.cpp>

TEST(ExTests, FindNodeWorksWhenPassedNullptr)
{
    ASSERT_EQ(find(nullptr, 1), false);
}

TEST(ExTests, EmplaceDoesNotExplodeWhenPassedNullptr)
{
    emplace(nullptr, 1);
    // No explosion? -> OK
    // (no memory allocations should happen here as well)
}

bool treeIsCorrect(const Node* node)
{
    if(node == nullptr)
        return true;

    const Node* left = node->left;
    const Node* right = node->right;

    if(left != nullptr && left->value >= node->value)
        return false;

    if(right != nullptr && right->value <= node->value)
        return false;

    return treeIsCorrect(left) && treeIsCorrect(right);
}

unsigned countNodes(const Node* node)
{
    if(node == nullptr)
        return 0;
        
    return 1 + countNodes(node->left) + countNodes(node->right);
}

void deleteTree(Node* node)
{
    if(node == nullptr)
        return;

    deleteTree(node->left);
    deleteTree(node->right);

    delete node;
}

TEST(ExTests, CanCreateCorrectBinaryTree)
{
    Node* root = new Node{ 0 };

    auto nums = { 0, 1, -5, 7, 2, 23132, -3213142 };

    for(auto n : nums)
    {
        emplace(root, n);
    }

    for(auto n : nums)
    {
        EXPECT_EQ(find(root, n), true);
    }

    EXPECT_EQ_MSG(treeIsCorrect(root), true);
    EXPECT_EQ_MSG(countNodes(root), nums.size())
    deleteTree(root);
}
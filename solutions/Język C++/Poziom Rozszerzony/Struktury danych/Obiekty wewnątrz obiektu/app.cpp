// You can do this!

// Code here...
#include <Node.hpp>

bool find(const Node* root, int n) {
    if (root == nullptr) return false;

    if (root->value == n) return true;
    else if (n < root->value) return find(root->left, n);
    else return find(root->right, n);
}

void emplace(Node* root, int n) {
    if (root == nullptr) return;  // ⛔ nic nie robimy!

    if (n < root->value) {
        if (root->left == nullptr)
            root->left = new Node{n};
        else
            emplace(root->left, n);
    } else if (n > root->value) {
        if (root->right == nullptr)
            root->right = new Node{n};
        else
            emplace(root->right, n);
    }
    // jeśli n == root->value — nic nie robimy (już jest w drzewie)
}
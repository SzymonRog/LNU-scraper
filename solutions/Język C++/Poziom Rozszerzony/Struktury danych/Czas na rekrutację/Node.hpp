#pragma once

#include <cstdint>

struct Node
{
    std::uint32_t data;
    Node* next{};
};
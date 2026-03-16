// Na razie nie zwracaj uwagi na tą linijkę :)
#pragma once
#include <string>

struct State
{
    std::string url;

    State* next{};
    State* prev{};
};
#pragma once

#include <string>

// Ten namespace zawiera rzeczy związane z sql (a masło jest maślane)
namespace sql
{

struct Part
{
    std::uint32_t id;

    std::string name;
    std::string manufacturer;
    std::string documentation; // link to documentation
    std::string location; // sector and shelf

    std::uint64_t stock;
};

}
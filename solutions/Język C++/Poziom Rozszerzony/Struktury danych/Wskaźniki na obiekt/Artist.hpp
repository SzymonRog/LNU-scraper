#pragma once

#include <string>

#include <Image.hpp>

// `Forward declaration` dla klasy Album
struct Album;

struct Artist
{
    std::string name;
    
    Album** albums{};
    size_t numOfAlbums;

    Image* profilePicture{};

    std::string biography;
    
    // To nie jest kompletna lista (brakuje np. gatunku, roku utworzenia...),
    // ale tyle wystarczy 'tutaj'
};
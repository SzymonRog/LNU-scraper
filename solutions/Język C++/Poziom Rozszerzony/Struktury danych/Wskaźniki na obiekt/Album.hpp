#pragma once

#include <string>

#include <Track.hpp>
#include <Image.hpp>

// `Forward declaration` dla klasy Artist
struct Artist;

struct Album
{
	std::string title;
	Image* coverArt{};
	Artist* artist{};
	
	size_t numOfTracks;
	Track** tracks{};
};
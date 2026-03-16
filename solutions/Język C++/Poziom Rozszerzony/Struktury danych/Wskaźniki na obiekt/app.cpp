// Your code here...
#include "Artist.hpp"
#include "Album.hpp"
#include "RandomUtils.hpp"
#include "Track.hpp"

Track* pickRandomTrack(const Artist& artist) {
    if (artist.numOfAlbums == 0 || artist.albums == nullptr) {
        return nullptr;
    }


    int albumIndex = getRandomInt(0, (artist.numOfAlbums) - 1);
    Album* selectedAlbum = artist.albums[albumIndex];

    if (selectedAlbum == nullptr || selectedAlbum->numOfTracks == 0 || selectedAlbum->tracks == nullptr) {
        return nullptr;
    }

   
    int trackIndex = getRandomInt(0, (selectedAlbum->numOfTracks) - 1);
    return selectedAlbum->tracks[trackIndex];
}



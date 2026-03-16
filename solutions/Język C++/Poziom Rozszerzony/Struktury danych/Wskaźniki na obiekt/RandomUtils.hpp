#pragma once



// Returns a random integer in the range [min, max]
int getRandomInt(int min, int max);



// Typ T zostanie określony przy kompilacji, o tej magii będzie później :)

// Returns a reference to a random element in the array
template< typename T >
T& getRandomElement(T* array, const size_t size);
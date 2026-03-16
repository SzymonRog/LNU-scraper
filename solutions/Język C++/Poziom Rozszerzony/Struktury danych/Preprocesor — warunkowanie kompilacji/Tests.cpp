// Force the user to be more precise with the header-guard name
#define COMPLEX
#define COMPLEX_H
#define complex
#define complex_h
#define TRIBOOL
#define TRIBOOL_H
#define tribool
#define tribool_h
#define LOGIC
#define MATH

// Faktycznie dołączam oba pliki :)
#include <Complex.hpp>
#include <Tribool.hpp>


TEST(itLives, itLives)
{
    // Check whether user hasn't just deleted definitions to omit the problem...
    math::Complex c;
    logic::Tribool t;
}
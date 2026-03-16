
#ifndef TRIBOOL_HPP   // Zabezpieczenie przed wielokrotnym dołączaniem
#define TRIBOOL_HPP

namespace logic
{

struct Tribool
{
    // Pozwala na przechowywanie trzech wartości:
    // true, false i indeterminate

    // Użyteczne, gdy coś może mieć faktycznie trzy stany, np. request
    // może 'być w stanie': success, failure lub pending
};

}
#endif

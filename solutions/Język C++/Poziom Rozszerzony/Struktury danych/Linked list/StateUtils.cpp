/* Funkcje next i prev nie przyjmują stałych wskaźników, bo wtedy
 * zwracany wskaźnik również musiałby być stały, a nie chcemy tego wymuszać
 *
 * Takie wymuszanie stałości 'wszędzie' nazywane jest 'const poisoning'.
 *
 *
 * Jeżeli chcielibyśmy mieć możliwość używania funkcji 'next' dla wskaźników
 * zwykłych i stałych musielibyśmy napisać dwa warianty funkcji o tej samej nazwie.
 */
#include <string>

#include <State.hpp>

State* next(State* state, unsigned int n)
{  
    if(!state)
        return nullptr;

    if(n == 0)
        return state;
    else
        return next(state->next, n - 1);
}

State* prev(State* state, unsigned int n)
{
    if(!state)
        return nullptr;

    if(n == 0)
        return state;
    else
        return prev(state->prev, n - 1);
}

void clearSuccesors(State* state)
{
    if(state->next != nullptr)
    {
        clearSuccesors(state->next);
        delete state->next;
    }
}

void addNext(State* state, std::string url)
{
    if(!state)
        return;

    clearSuccesors(state);

    state->next = new State{ url };
    state->next->prev = state;
}

void insert(State* state, std::string url)
{
    if(!state)
        return;
        
    State* next = state->next;
    State* newState = new State;
    newState->url = url;
    newState->prev = state;
    newState->next = next;
    
    state->next = newState;
    
    if(next)
        next->prev = newState;
}










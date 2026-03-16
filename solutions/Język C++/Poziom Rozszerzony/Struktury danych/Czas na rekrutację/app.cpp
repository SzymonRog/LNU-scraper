// Spróbuj rozwiązać problem przechodząc po elementach co najwyżej raz (rekruter patrzy)
#include <Node.hpp>

const Node* findMiddle(const Node* head) {
    if (!head) return nullptr;  // Jeśli lista jest pusta, zwróć nullptr

    const Node* slow = head;  // Wskaźnik wolniejszy
    const Node* fast = head;  // Wskaźnik szybszy

    // Dopóki fast i fast->next są różne od nullptr
    while (fast && fast->next) {
        slow = slow->next;      // Przesuwamy slow o jeden krok
        fast = fast->next->next; // Przesuwamy fast o dwa kroki
    }

    // Jeśli fast jest nullptr, oznacza to, że lista ma parzystą liczbę elementów,
    // a slow wskazuje na drugi element z dwóch środkowych. W takim przypadku zwrócimy
    // poprzedni element.
    if (!fast) {
        const Node* prev = head;
        while (prev->next != slow) {
            prev = prev->next;
        }
        return prev;  // Zwracamy poprzedni element, który jest przed środkowym
    }

    // Zwracamy slow, który wskazuje na środkowy element, gdy lista ma nieparzystą liczbę elementów
    return slow;
}
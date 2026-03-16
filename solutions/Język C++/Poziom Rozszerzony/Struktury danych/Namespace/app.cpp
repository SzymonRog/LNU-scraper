// Do your best!

/* Normalnie, o tym z których pinów i kiedy można odczytywać napięcie
 * można przeczytać w dokumentacji, ale mikrokontroler przecież nie 
 * istnieje, a my żyjemy w symulacji (patrz C++ level 3) więc...
 *
 * Konwerter sygnału analogowego na cyfrowy jest dostępny przy pinach o ID:
 * 4-7, 11-16 i 18
 * Obiekty typu Pin posiadają informację o swoim id w polu 'id'.
 * 
 * Możliwe stany pinu definiuje enum zawarty w strukturze Pin, dostępny 
 * poprzez Pin::Mode. Stan pina zawarty jest w polu 'mode'.
 * Napięcie można odczytać tylko z pinów ustawionych jako Input. (Pin::Mode::Input)
 */
#include <Pin.hpp>
#include <Adc.hpp>
#include <cmath> // Dla zaokrąglenia do jednej liczby po przecinku

namespace PinUtils
{
    // Funkcja sprawdzająca, czy pin jest przypisany do ADC
    bool isAdcEnabled(const GPIO::Pin& pin)
    {
        // Definicja pinów, które są przypisane do ADC
        // Przykładowe ID pinów, które są przypisane do ADC
        const int adcEnabledIds[] = {4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 18};

        // Sprawdzamy, czy pin należy do puli poprawnych ID
        for (int i = 0; i < sizeof(adcEnabledIds) / sizeof(adcEnabledIds[0]); ++i)
        {
            if (pin.id == adcEnabledIds[i])
            {
                return true; // Pin jest przypisany do ADC
            }
        }

        return false; // Pin nie jest przypisany do ADC
    }

    // Funkcja do obliczenia napięcia z ADC
    float getPinVoltage(const GPIO::Pin& pin)
    {
        // Sprawdzamy, czy pin jest ustawiony na tryb wejścia (Input) i czy jest przypisany do ADC
        if (pin.mode == GPIO::Pin::Mode::Input && isAdcEnabled(pin))
        {
            // Odczytujemy wartość z ADC
            unsigned int v = GPIO::adcRead(pin);

            // Obliczamy napięcie: v / 1023 * 5, ponieważ ADC ma rozdzielczość 10 bitów
            float voltage = static_cast<float>(v) * 5.0f / 1023.0f;

            // Zaokrąglamy wynik do jednej liczby po przecinku
            return std::round(voltage * 10.0f) / 10.0f;
        }
        else
        {
            // Jeśli pin nie jest poprawny, zwracamy 0.0
            return 0.0f;
        }
    }
}
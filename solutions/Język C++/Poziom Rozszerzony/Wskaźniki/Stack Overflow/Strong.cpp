/* Nie wywołujesz tej funkcji;
 * Jest to jedynie przykład "jak zrobić to lepiej"
 */

unsigned int calcStrong(unsigned int n, unsigned int mod)
{
    unsigned int result = 1;
    
    // Nie wywołujemy żadnej funkcji, obliczamy silnię 'iteracyjnie'
    for(int i = 1; i < n; i++)
    {
        result = (result * i) % mod;
    }
    
    return result;
}
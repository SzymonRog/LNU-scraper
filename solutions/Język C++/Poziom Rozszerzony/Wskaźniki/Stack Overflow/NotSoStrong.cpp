/* Funkcja jest rekurencyjna, czyli wywołuje samą siebie.
 * Dla n = 2 funkcja zostanie wywołana 2 razy (dla 1 i 2)
 * Dla n funkcja zostanie wywołana dla (n, n-1, n-2, ..., 1)
 * 
 * Zauważ, że pierwsza zakończy działanie funkcja wywołana dla n=1
 */
unsigned int calcStrong(unsigned int n, unsigned int mod)
{
    if(n == 1)
        return 1;

    return (calcStrong(n-1, mod) * n) % mod;
}

// Twój "wrapper" dla funkcji calcStrong
unsigned int safeStrong(unsigned int n, unsigned int mod)
{
    
    const unsigned int MAX_RECURSION_DEPTH = 262144;
    
    if(n > MAX_RECURSION_DEPTH) return 0 ;
    return calcStrong(n, mod);
}

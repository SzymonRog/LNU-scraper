
int* getNumberSum(int num) {
    int sum = 0;
    num = abs(num); // Ignorujemy znak liczby
    
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    
    int* result = (int*)malloc(sizeof(int)); // Dynamiczna alokacja pamięci
    if (result != NULL) {
        *result = sum;
    }
    
    return result;
}
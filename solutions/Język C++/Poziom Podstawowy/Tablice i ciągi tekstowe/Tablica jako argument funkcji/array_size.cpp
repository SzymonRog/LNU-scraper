void array_size ( int results [10] )
{
   int results_copy[10];

   // kopiujemy tablicę results do results_copy
   for ( int i = 0; i < 10; i++ )
       results_copy[i] = results[i];

   // wyświetlamy rozmiary tablic results oraz results_copy
   std::cout << "Rozmiar sizeof() tablicy results = " << sizeof(results) << std::endl;
   std::cout << "Rozmiar sizeof() tablicy results_copy = " << sizeof(results_copy) << std::endl;

   //Liczba elementów tablicy results
   std::cout << "Liczba elementów tablicy results = " << sizeof(results) / sizeof(results[0]) << std::endl;

   //Liczba elementów tablicy results_copy
   std::cout << "Liczba elementów tablicy results_copy = " << sizeof(results_copy) / sizeof(results_copy[0]) << std::endl;
}

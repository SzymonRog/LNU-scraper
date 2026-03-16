/* Popatrz na przebieg działania programu i na to jak po kolei wygląda stack
 * Program zaczyna się w main, następnie wywoła funkcje a i b
 */


void b(int* a/*[5]*/, char c/*[6]*/)
{
/* Zmienna na którą wskazuje a nie jest kopiowana, 
 * ale wskaźnik na nią musi zostać gdzieś umieszczony
 *
 *Stos pamięci:
 * -> [b] ([5]int*, [6]char, [7]{long long, long long, long long})
 * [a] ([3]string, [4]int)
 * [main] ([1]int, [2]int)
 */

    cout << *a << " " << c << endl;
    long long /*[7]*/ arr[3];
    /* ... */
}

void a()
{
/* Stos pamięci:
 * -> [a] ([3]string, [4]int)
 * [main] ([1]int, [2]int)
 */

    string word; // [3]
    cin >> word;

    int wordLength /*[4]*/ = word.length();
    b(wordLength, word[0]);
    
    // Ta zmienna trafia na heap
    unsigned int a = new unsigned int(wordLength);
}

int main()
{
/* Stos pamięci:
 * -> [main] ([1]int, [2]int)
*/

    int n; // [1]
    cin >> n;

    for(int i /*[2]*/ = 0; i < n; i++)
    {
        a();
    }

}
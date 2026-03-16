// Co wypisze następujący program?

#include <iostream>

using namespace std;

int main()
{
    int num = 1;
    int& ref = num;

    cout << num << " " << ref << '\n';

    int y = 3;
    ref = y;
    y = 5;

    cout << num << " " << ref << '\n';

    num = 7;

    cout << num << " " << ref << '\n';
}


/* Odpowiedź poniżej
          
          ||
          ||
          ||
          ||
          ||
         \  /
          \/



































Wyjście programu:
1 1
3 3
7 7

*/
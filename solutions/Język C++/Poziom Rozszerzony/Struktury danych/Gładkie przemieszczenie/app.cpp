#include <ObjectPosition.hpp>
#include <algorithm>
using namespace std;

/* Funkcja wywołana zostanie raz, gdy punkt doświadczenia powinien zacząć się przesuwać.
 * Tuż po wywołaniu tej funkcji, updatePosition() zostanie wywołane.
 *
 * @param worldTime - czas w sekundach, który upłynął od uruchomienia poziomu
 * @param pointPosition - pozycja punktu doświadczenia
*/
double startX, startY;
double spawnTime;
void init(const float worldTime, const ObjectPosition& pointPosition)
{
    spawnTime = worldTime;
    startX = pointPosition.x;
    startY = pointPosition.y;

}

/* Wywoływana podczas ruchu punktu. 
 * Punkt zostanie usunięty, gdy zdeży się z obiektem (funkcja nie będzie później wywoływana)
 *
 * @param worldTime - czas w sekundach, który upłynął od uruchomienia poziomu
 * @param pointPosition - pozycja punktu doświadczenia
 * @param playerPosition - pozycja gracza
 */
void updatePosition(
    const float worldTime, 
    ObjectPosition& pointPosition, 
    const ObjectPosition& playerPosition)
{
    double t = (worldTime - spawnTime) /2.0;
    if( t >= 1.0){
        pointPosition.x = playerPosition.x;
        pointPosition.y = playerPosition.y;
        return;
    }
    
    
    pointPosition.x = startX + t *(playerPosition.x - startX);
    pointPosition.y = startY + t *(playerPosition.y - startY);
    
}
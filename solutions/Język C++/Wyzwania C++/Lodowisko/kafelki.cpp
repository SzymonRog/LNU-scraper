#include <cmath>

void kafelki(double R, int &c, int &p) {
    c = 0;
    p = 0;
    
    int maxTile = (int)ceil(R);
    
    for (int x = 0; x < maxTile; x++) {
        for (int y = 0; y < maxTile; y++) {
            // Narożniki kafelka (x, y)
            double d1 = x*x + y*y;
            double d2 = (x+1)*(x+1) + y*y;
            double d3 = x*x + (y+1)*(y+1);
            double d4 = (x+1)*(x+1) + (y+1)*(y+1);
            
            double R2 = R * R;
            
            bool anyInside = (d1 < R2) || (d2 < R2) || (d3 < R2) || (d4 < R2);
            bool allInside = (d1 <= R2) && (d2 <= R2) && (d3 <= R2) && (d4 <= R2);
            
            if (allInside) {
                c++;
            } else if (anyInside) {
                p++;
            }
        }
    }
    
    // Symetria czterech ćwiartek
    c *= 4;
    p *= 4;
}
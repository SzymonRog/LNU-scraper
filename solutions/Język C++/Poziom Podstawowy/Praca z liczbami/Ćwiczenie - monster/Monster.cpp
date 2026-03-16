#define MONSTER unsigned char

const unsigned char monsterHasGun          =   1;
const unsigned char monsterIsAggresive     =   2;
const unsigned char monsterIsFireResistant =   4;
const unsigned char monsterLoseWeapon      =   8;
const unsigned char monsterSeeOponent      =  16;
const unsigned char monsterHearOponent     =  32;
const unsigned char monsterRunOponent      =  64;
const unsigned char monsterOpenDoor        = 128;

MONSTER setMonster ( bool param1, bool param2, bool param3, bool param4, bool param5, bool param6, bool param7, bool param8 )
{
    unsigned char bit = 0;
    if (param1) bit += 1;
    if (param2) bit += 2;
    if (param3) bit += 4;
    if (param4) bit += 8;
    if (param5) bit += 16;
    if (param6) bit += 32;
    if (param7) bit += 64;
    if (param8) bit += 128;
    
    return bit;
   
}

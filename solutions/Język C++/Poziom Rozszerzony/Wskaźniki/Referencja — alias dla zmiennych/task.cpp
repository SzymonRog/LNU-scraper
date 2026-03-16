int* prodValOfKTLPaintSec;

int getCoef()
{
    if (prodValOfKTLPaintSec == nullptr)
        return 0;

    int& val = *prodValOfKTLPaintSec;

    if (val >= 120)
        return 1;

    if (val >= 150)
        return 2;

    return -1;
}

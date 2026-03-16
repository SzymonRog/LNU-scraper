#include <DatabaseUtils.hpp>
#include <string>
using namespace std;

string getProductNamesList(int* ids, size_t arrLen)
{
    
    string* productNames = new string[arrLen];

    
    for (size_t i = 0; i < arrLen; ++i) {
        productNames[i] = getProductName(ids[i]);
    }

    
    return flattenStringArray(productNames, arrLen);
}
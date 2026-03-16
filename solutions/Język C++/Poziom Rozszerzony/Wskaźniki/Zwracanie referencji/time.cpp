#include <string>

using namespace std;

string& addDateToString(string& str, unsigned int h, unsigned int m)
{
    str += (h < 10 ? "0" : "") + to_string(h) + ':';
    str += (m < 10 ? "0" : "") + to_string(m);
    return str;
}
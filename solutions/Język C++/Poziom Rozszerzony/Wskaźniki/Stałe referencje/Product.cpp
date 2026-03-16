// Za niedługo nie będzie nawet tego...
#include <string>
#include <cctype> 
using namespace std;

bool isProdNameValid(const string& name){
    for(char ch : name){
        if(!(isalnum(ch) || ch == '_' || ch == ' ' || ch == '-' )){
            return false;
        }
    }
    return true;
}
/* Notka:
 * Może są jakieś funkcje w c++, które ci w tym pomogą.
 * Zawsze warto sprawdzić...
 */
 
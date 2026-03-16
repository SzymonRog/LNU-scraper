//c++
#include <string>
using namespace std;


bool testFizzBuzz(int questions[], string answers[], int len)
{
    for( int i = 0; i < len; i ++){
        int number = questions[i];
        
        if(number % 3 == 0 and number % 5 == 0){
            if(answers[i] != "FizzBuzz"){
                return false;
            }
            
        }else if(number % 3 == 0){
            if(answers[i] != "Fizz"){
                return false;
            }
            
        }else if(number % 5 == 0){
            if(answers[i] != "Buzz"){
                return false;
            }
            
        }else{
            if(answers[i] != to_string(number)){
                return false;
            }
        }
        
    }
    
    return true;
}
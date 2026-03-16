/* Tak może wyglądać kod testujący twój kod;
 * może -> może tak może nie
 */

#include <RandomUtils.hpp>
#include <TextFormattingTools.cpp>
#include <Database.hpp>

#include <LoginPage.cpp>



#include <SecretAnswerGenerator.hpp>



// Testy z poprzedniej lekcji
bool normalTest()
{
    std::string str = generateString({alphanum, special, ' '});
    std::string strForUser = str;
    
    const bool answer = getAnsForIsLoginUsed(&strForUser);
    
    removeWhitespaces(&str);
    toLowerCase(&str);
    const bool expected = isLoginUsed(&str);
    
    return answer == expected;
}

// Test do sprawdzenia zachowania funkcji gdy przekazany zostanie nullptr
bool deviousTest()
{
    const bool answer = getAnsForIsLoginUsed(nullptr);
    const bool expected = false;
    
    return answer == expected;
}


// W "rzeczywistości" do wykonywania testów najczęściej używa się specjalnych bibliotek.
// Coś o tym na pewno będzie w dalszej części kursu

// (to... gdzie teraz jesteśmy, jeżeli nie w rzeczywistości? ~redaktor)
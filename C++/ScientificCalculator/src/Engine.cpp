#include "Engine.h"

#include "FunctionLibrary.h"
#include "Tokenizer.h"
#include "Parser.h"

#include <string>
#include <vector>

using namespace std;



// =======================
// Initialize
// =======================

void Engine::initialize()
{

    static bool initialized =
        false;


    if(initialized)
        return;


    FunctionLibrary::initialize();


    initialized = true;

}



// =======================
// Evaluate
// =======================

double Engine::evaluate(
    const string& expression
)
{

    initialize();


    Tokenizer tokenizer(
        expression
    );


    vector<string> tokens =
        tokenizer.tokenize();


    Parser parser(
        tokens
    );


    return parser.evaluate();

}

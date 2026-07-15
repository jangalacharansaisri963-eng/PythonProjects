#include "FunctionLibrary.h"

#include <stdexcept>


using namespace std;


// =======================
// Storage
// =======================

FunctionMap
FunctionLibrary::FUNCTIONS;



// =======================
// Register Function
// =======================

void FunctionLibrary::registerFunction(
    const string& name,
    MathFunction function
)
{

    FUNCTIONS[name] =
        function;

}



// =======================
// Exists
// =======================

bool FunctionLibrary::exists(
    const string& name
)
{

    return
        FUNCTIONS.find(name)
        != FUNCTIONS.end();

}



// =======================
// Call Function
// =======================

double FunctionLibrary::call(
    const string& name,
    const MathArguments& arguments
)
{

    auto iterator =
        FUNCTIONS.find(name);


    if(
        iterator ==
        FUNCTIONS.end()
    )
    {

        throw runtime_error(
            "Unknown function: " +
            name
        );

    }


    return
        iterator->second(
            arguments
        );

}



// =======================
// Initialize
// =======================

void FunctionLibrary::initialize()
{

    FUNCTIONS.clear();


    // ==================================
    // Built-in functions register here.
    //
    // Example later:
    //
    // Roots::registerFunctions();
    // Trigonometry::registerFunctions();
    // Logarithms::registerFunctions();
    // Powers::registerFunctions();
    // Factorial::registerFunctions();
    // Random::registerFunctions();
    // Memory::registerFunctions();
    //
    // Every module registers itself.
    // ==================================

}

#include "FunctionLibrary.h"

#include "functions/Arithmetic.h"
#include "functions/Roots.h"
#include "functions/Powers.h"
#include "functions/Trigonometry.h"
#include "functions/Hyperbolic.h"
#include "functions/Logarithms.h"
#include "functions/Factorial.h"
#include "functions/Random.h"
#include "functions/Memory.h"

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


    Arithmetic::registerFunctions();

    Roots::registerFunctions();

    Powers::registerFunctions();

    Trigonometry::registerFunctions();

    Hyperbolic::registerFunctions();

    Logarithms::registerFunctions();

    Factorial::registerFunctions();

    Random::registerFunctions();

    Memory::registerFunctions();

}

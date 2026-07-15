#include "Hyperbolic.h"

#include "../FunctionLibrary.h"

#include <cmath>
#include <stdexcept>

using namespace std;



void Hyperbolic::registerFunctions()
{

    FunctionLibrary::registerFunction(
        "sinh",
        Hyperbolic::sinh
    );

    FunctionLibrary::registerFunction(
        "cosh",
        Hyperbolic::cosh
    );

    FunctionLibrary::registerFunction(
        "tanh",
        Hyperbolic::tanh
    );

}



double Hyperbolic::sinh(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "sinh requires 1 argument"
        );

    return std::sinh(
        arguments[0]
    );

}



double Hyperbolic::cosh(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "cosh requires 1 argument"
        );

    return std::cosh(
        arguments[0]
    );

}



double Hyperbolic::tanh(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "tanh requires 1 argument"
        );

    return std::tanh(
        arguments[0]
    );

}

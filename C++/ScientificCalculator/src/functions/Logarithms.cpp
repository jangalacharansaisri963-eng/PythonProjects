#include "Logarithms.h"

#include "../FunctionLibrary.h"

#include <cmath>
#include <stdexcept>

using namespace std;



void Logarithms::registerFunctions()
{

    FunctionLibrary::registerFunction(
        "ln",
        Logarithms::ln
    );

    FunctionLibrary::registerFunction(
        "lg",
        Logarithms::lg
    );

}



double Logarithms::ln(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "ln requires 1 argument"
        );

    if(arguments[0] <= 0)
        throw runtime_error(
            "ln undefined for values <= 0"
        );

    return std::log(
        arguments[0]
    );

}



double Logarithms::lg(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "lg requires 1 argument"
        );

    if(arguments[0] <= 0)
        throw runtime_error(
            "lg undefined for values <= 0"
        );

    return std::log10(
        arguments[0]
    );

}

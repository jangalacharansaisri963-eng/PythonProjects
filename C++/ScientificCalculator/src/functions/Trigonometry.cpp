#include "Trigonometry.h"

#include "../FunctionLibrary.h"

#include <cmath>
#include <stdexcept>

using namespace std;



void Trigonometry::registerFunctions()
{

    FunctionLibrary::registerFunction(
        "sin",
        Trigonometry::sin
    );

    FunctionLibrary::registerFunction(
        "cos",
        Trigonometry::cos
    );

    FunctionLibrary::registerFunction(
        "tan",
        Trigonometry::tan
    );

}



double Trigonometry::sin(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "sin requires 1 argument"
        );

    return std::sin(
        arguments[0]
    );

}



double Trigonometry::cos(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "cos requires 1 argument"
        );

    return std::cos(
        arguments[0]
    );

}



double Trigonometry::tan(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "tan requires 1 argument"
        );

    return std::tan(
        arguments[0]
    );

}

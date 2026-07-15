#include "Powers.h"

#include "../FunctionLibrary.h"

#include <cmath>
#include <stdexcept>

using namespace std;



void Powers::registerFunctions()
{

    FunctionLibrary::registerFunction(
        "square",
        Powers::square
    );

    FunctionLibrary::registerFunction(
        "cube",
        Powers::cube
    );

    FunctionLibrary::registerFunction(
        "pow",
        Powers::power
    );

    FunctionLibrary::registerFunction(
        "tenpow",
        Powers::tenPower
    );

    FunctionLibrary::registerFunction(
        "epow",
        Powers::ePower
    );

}



double Powers::square(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "square requires 1 argument"
        );

    return arguments[0] * arguments[0];

}



double Powers::cube(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "cube requires 1 argument"
        );

    return arguments[0] *
           arguments[0] *
           arguments[0];

}



double Powers::power(
    const MathArguments& arguments
)
{

    if(arguments.size() != 2)
        throw runtime_error(
            "pow requires 2 arguments"
        );

    return std::pow(
        arguments[0],
        arguments[1]
    );

}



double Powers::tenPower(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "tenpow requires 1 argument"
        );

    return std::pow(
        10.0,
        arguments[0]
    );

}



double Powers::ePower(
    const MathArguments& arguments
)
{

    if(arguments.size() != 1)
        throw runtime_error(
            "epow requires 1 argument"
        );

    return std::exp(
        arguments[0]
    );

}

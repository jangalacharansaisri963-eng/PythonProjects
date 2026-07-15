#ifndef FACTORIAL_H
#define FACTORIAL_H

#include "../Types.h"

class Factorial
{

public:

    static void registerFunctions();

    static double factorial(
        const MathArguments& arguments
    );

};

#endif

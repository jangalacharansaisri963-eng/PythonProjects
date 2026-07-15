#ifndef ARITHMETIC_H
#define ARITHMETIC_H

#include "../Types.h"

class Arithmetic
{

public:

    static void registerFunctions();

    static double abs(
        const MathArguments& arguments
    );

    static double reciprocal(
        const MathArguments& arguments
    );

    static double negate(
        const MathArguments& arguments
    );

};

#endif

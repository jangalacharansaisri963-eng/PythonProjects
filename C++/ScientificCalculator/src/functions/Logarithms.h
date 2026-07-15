#ifndef LOGARITHMS_H
#define LOGARITHMS_H

#include "../Types.h"

class Logarithms
{

public:

    static void registerFunctions();

    static double ln(
        const MathArguments& arguments
    );

    static double lg(
        const MathArguments& arguments
    );

};

#endif

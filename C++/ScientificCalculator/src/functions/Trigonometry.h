#ifndef TRIGONOMETRY_H
#define TRIGONOMETRY_H

#include "../Types.h"

class Trigonometry
{

public:

    static void registerFunctions();

    static double sin(
        const MathArguments& arguments
    );

    static double cos(
        const MathArguments& arguments
    );

    static double tan(
        const MathArguments& arguments
    );

};

#endif

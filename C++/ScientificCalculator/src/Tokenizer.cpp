#include "Tokenizer.h"

#include <cctype>
#include <stdexcept>


vector<string> tokenize(
    const string& expression
)
{

    vector<string> tokens;


    for(size_t i = 0; i < expression.length();)
    {

        char c = expression[i];


        // Ignore spaces

        if(isspace(c))
        {
            i++;
            continue;
        }



        // Numbers

        if(
            isdigit(c) ||
            c == '.'
        )
        {

            string number;


            while(
                i < expression.length() &&
                (
                    isdigit(expression[i]) ||
                    expression[i] == '.'
                )
            )
            {

                number += expression[i];

                i++;

            }


            tokens.push_back(number);

            continue;
        }



        // Names:
        // sqrt, sin, root, pi, e

        if(isalpha(c))
        {

            string name;


            while(
                i < expression.length() &&
                isalpha(expression[i])
            )
            {

                name += expression[i];

                i++;

            }


            tokens.push_back(name);

            continue;
        }



        // Operators and brackets

        if(
            c == '+' ||
            c == '-' ||
            c == '*' ||
            c == '/' ||
            c == '%' ||
            c == '^' ||
            c == '(' ||
            c == ')' ||
            c == ','
        )
        {

            tokens.push_back(
                string(1,c)
            );

            i++;

            continue;
        }



        throw runtime_error(
            string("Unknown character: ") + c
        );

    }


    return tokens;
}

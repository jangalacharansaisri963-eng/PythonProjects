#include <iostream>
#include <string>

#include "Engine.h"

using namespace std;


int main()
{

    cout << "Scientific Calculator C++\n";
    cout << "Type exit to quit\n\n";


    string expression;


    while(true)
    {

        cout << "> ";

        getline(
            cin,
            expression
        );


        if(
            expression == "exit" ||
            expression == "quit"
        )
        {
            break;
        }


        if(expression.empty())
        {
            continue;
        }


        try
        {

            double result =
                Engine::evaluate(
                    expression
                );


            cout
                << "= "
                << result
                << "\n";

        }


        catch(exception &e)
        {

            cout
                << "Error: "
                << e.what()
                << "\n";

        }

    }


    return 0;

}

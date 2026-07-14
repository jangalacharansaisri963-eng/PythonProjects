#include <iostream>
#include <string>

#include "Parser.h"
#include "Tokenizer.h"


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

            vector<string> tokens =
                tokenize(expression);


            Parser parser(tokens);


            double result =
                parser.evaluate();


            cout << "= "
                 << result
                 << "\n";

        }


        catch(exception &e)
        {

            cout << "Error: "
                 << e.what()
                 << "\n";

        }

    }


    return 0;
}

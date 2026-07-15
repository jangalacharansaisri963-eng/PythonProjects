#ifndef PARSER_H
#define PARSER_H

#include <string>
#include <vector>


class Parser
{

private:

    std::vector<std::string> tokens;

    std::size_t position = 0;


    // =======================
    // Grammar
    // =======================

    double parseExpression();

    double parseTerm();

    double parsePower();

    double parseUnary();

    double parsePrimary();


    // =======================
    // Helpers
    // =======================

    bool isAtEnd() const;

    std::string peek() const;

    std::string advance();

    bool match(
        const std::string& token
    );



public:

    Parser(
        const std::vector<std::string>& tokens
    );

    double evaluate();

};

#endif

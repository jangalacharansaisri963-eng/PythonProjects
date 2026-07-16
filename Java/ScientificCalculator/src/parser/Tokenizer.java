package parser;

import java.util.ArrayList;
import java.util.List;


public class Tokenizer {


    // ==========================
    // Tokenize Expression
    // ==========================

    public static List<String> tokenize(
            String expression
    ) {

        List<String> tokens =
                new ArrayList<>();


        StringBuilder number =
                new StringBuilder();


        for (int i = 0; i < expression.length(); i++) {

            char c =
                    expression.charAt(i);


            // ==========================
            // Numbers
            // ==========================

            if (
                Character.isDigit(c)
                || c == '.'
            ) {

                number.append(c);
                continue;
            }


            // Finish number before operator

            if (number.length() > 0) {

                tokens.add(
                    number.toString()
                );

                number.setLength(0);
            }


            // ==========================
            // Spaces
            // ==========================

            if (
                Character.isWhitespace(c)
            ) {
                continue;
            }


            // ==========================
            // Operators
            // ==========================

            if (
                c == '+'
                || c == '-'
                || c == '*'
                || c == '/'
                || c == '('
                || c == ')'
            ) {

                tokens.add(
                    String.valueOf(c)
                );

            }

            else {

                throw new RuntimeException(
                    "Unknown character: " + c
                );
            }

        }


        // Add final number

        if (number.length() > 0) {

            tokens.add(
                number.toString()
            );
        }


        return tokens;
    }

}

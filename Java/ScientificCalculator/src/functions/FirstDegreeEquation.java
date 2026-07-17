package functions;

import java.util.List;

import parser.EquationTokenizer;
import parser.EquationParser;
import parser.LinearExpression;


/*
 * FirstDegreeEquation
 *
 * Solves equations of the form:
 *
 * ax + b = cx + d
 *
 * Examples:
 *
 * 2x+4=10
 * 3x-5=2x+9
 * 4(x-3)+5=2(x+1)
 *
 */

public class FirstDegreeEquation {


    // ==========================
    // Solve equation
    // ==========================

    public static double solve(
            String equation
    ) {


        String[] sides =
                equation.split("=");


        if (sides.length != 2) {

            throw new IllegalArgumentException(
                "Equation must contain one = sign"
            );

        }



        LinearExpression left =
                parseSide(
                    sides[0]
                );


        LinearExpression right =
                parseSide(
                    sides[1]
                );



        // Move everything left:
        //
        // ax+b - (cx+d)=0

        double coefficient =
                left.getCoefficient()
                -
                right.getCoefficient();


        double constant =
                left.getConstant()
                -
                right.getConstant();



        if (coefficient == 0) {


            if (constant == 0) {

                throw new ArithmeticException(
                    "Infinite solutions"
                );

            }


            throw new ArithmeticException(
                "No solution"
            );

        }



        return -constant / coefficient;

    }



    // ==========================
    // Parse one side
    // ==========================

    private static LinearExpression parseSide(
            String side
    ) {


        List<String> tokens =
                EquationTokenizer.tokenize(
                        side
                );


        EquationParser parser =
                new EquationParser(
                        tokens
                );


        return parser.parse();

    }

}

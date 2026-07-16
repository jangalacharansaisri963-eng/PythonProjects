import java.util.List;

import parser.Tokenizer;
import parser.Parser;


public class Engine {


    // ==========================
    // Evaluate Expression
    // ==========================

    public static double evaluate(
            String expression
    ) {


        List<String> tokens =
                Tokenizer.tokenize(
                    expression
                );


        Parser parser =
                new Parser(
                    tokens
                );


        return parser.parse();

    }

}

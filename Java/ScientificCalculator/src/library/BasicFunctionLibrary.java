package library;

import functions.Logarithms;
import functions.Roots;
import functions.Trigonometry;

/*
 * BasicFunctionLibrary
 *
 * Registers the standard one-argument
 * mathematical functions.
 */

public class BasicFunctionLibrary {

    public static void register() {

        // ==========================
        // Roots
        // ==========================

        FunctionLibrary.register(
                "sqrt",
                args -> {

                    requireArguments(
                            "sqrt",
                            args.size(),
                            1
                    );

                    return Roots.sqrt(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "cbrt",
                args -> {

                    requireArguments(
                            "cbrt",
                            args.size(),
                            1
                    );

                    return Roots.cbrt(
                            args.get(0)
                    );

                }
        );

        // ==========================
        // Logarithms
        // ==========================

        FunctionLibrary.register(
                "ln",
                args -> {

                    requireArguments(
                            "ln",
                            args.size(),
                            1
                    );

                    return Logarithms.ln(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "log",
                args -> {

                    requireArguments(
                            "log",
                            args.size(),
                            1
                    );

                    return Logarithms.log(
                            args.get(0)
                    );

                }
        );

        // ==========================
        // Trigonometry
        // ==========================

        FunctionLibrary.register(
                "sin",
                args -> {

                    requireArguments(
                            "sin",
                            args.size(),
                            1
                    );

                    return Trigonometry.sin(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "cos",
                args -> {

                    requireArguments(
                            "cos",
                            args.size(),
                            1
                    );

                    return Trigonometry.cos(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "tan",
                args -> {

                    requireArguments(
                            "tan",
                            args.size(),
                            1
                    );

                    return Trigonometry.tan(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "arcsin",
                args -> {

                    requireArguments(
                            "arcsin",
                            args.size(),
                            1
                    );

                    return Trigonometry.arcsin(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "arccos",
                args -> {

                    requireArguments(
                            "arccos",
                            args.size(),
                            1
                    );

                    return Trigonometry.arccos(
                            args.get(0)
                    );

                }
        );

        FunctionLibrary.register(
                "arctan",
                args -> {

                    requireArguments(
                            "arctan",
                            args.size(),
                            1
                    );

                    return Trigonometry.arctan(
                            args.get(0)
                    );

                }
        );

    }

    // ==========================
    // Argument Checker
    // ==========================

    private static void requireArguments(
            String function,
            int received,
            int expected
    ) {

        if (received != expected) {

            throw new RuntimeException(
                    function
                    + "() expects "
                    + expected
                    + " argument(s)"
            );

        }

    }

}

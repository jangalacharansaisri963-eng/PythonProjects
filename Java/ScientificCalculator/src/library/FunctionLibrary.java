package library;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * FunctionLibrary
 *
 * Main registry for all calculator functions and constants.
 */

public class FunctionLibrary {

    // =========================================
    // Function Interface
    // =========================================

    @FunctionalInterface
    public interface CalculatorFunction {

        double apply(List<Double> arguments);

    }

    // =========================================
    // Function Registry
    // =========================================

    public static final Map<String, CalculatorFunction> FUNCTIONS =
            new HashMap<>();

    // =========================================
    // Constant Registry
    // =========================================

    public static final Map<String, Double> CONSTANTS =
            new HashMap<>();

    // =========================================
    // Initialize
    // =========================================

    public static void initialize() {

        FUNCTIONS.clear();

        CONSTANTS.clear();

        BasicFunctionLibrary.register();

        AdvancedFunctionLibrary.register();

        EquationFunctionLibrary.register();

        ConstantLibrary.register();

    }

    // =========================================
    // Register Function
    // =========================================

    public static void register(
            String name,
            CalculatorFunction function
    ) {

        FUNCTIONS.put(
                name.toLowerCase(),
                function
        );

    }

    // =========================================
    // Register Constant
    // =========================================

    public static void registerConstant(
            String name,
            double value
    ) {

        CONSTANTS.put(
                name.toLowerCase(),
                value
        );

    }

    // =========================================
    // Function Exists
    // =========================================

    public static boolean exists(
            String name
    ) {

        return FUNCTIONS.containsKey(
                name.toLowerCase()
        );

    }

    // =========================================
    // Constant Exists
    // =========================================

    public static boolean constantExists(
            String name
    ) {

        return CONSTANTS.containsKey(
                name.toLowerCase()
        );

    }

    // =========================================
    // Call Function
    // =========================================

    public static double call(
            String name,
            List<Double> arguments
    ) {

        CalculatorFunction function =
                FUNCTIONS.get(
                        name.toLowerCase()
                );

        if (function == null) {

            throw new RuntimeException(
                    "Unknown function: " + name
            );

        }

        return function.apply(arguments);

    }

    // =========================================
    // Get Constant
    // =========================================

    public static double constant(
            String name
    ) {

        Double value =
                CONSTANTS.get(
                        name.toLowerCase()
                );

        if (value == null) {

            throw new RuntimeException(
                    "Unknown constant: " + name
            );

        }

        return value;

    }

}

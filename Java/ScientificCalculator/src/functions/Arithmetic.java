package functions;

public class Arithmetic {


    // ==========================
    // Addition
    // ==========================

    public static double add(
            double a,
            double b
    ) {
        return a + b;
    }


    // ==========================
    // Subtraction
    // ==========================

    public static double subtract(
            double a,
            double b
    ) {
        return a - b;
    }


    // ==========================
    // Multiplication
    // ==========================

    public static double multiply(
            double a,
            double b
    ) {
        return a * b;
    }


    // ==========================
    // Division
    // ==========================

    public static double divide(
            double a,
            double b
    ) {

        if (b == 0) {
            throw new ArithmeticException(
                "Division by zero"
            );
        }

        return a / b;
    }


    // ==========================
    // Square Root
    // ==========================

    public static double sqrt(
            double x
    ) {

        if (x < 0) {
            throw new ArithmeticException(
                "Cannot calculate square root of negative number"
            );
        }

        return Math.sqrt(x);
    }


    // ==========================
    // Cube Root
    // ==========================

    public static double cbrt(
            double x
    ) {

        return Math.cbrt(x);
    }

}

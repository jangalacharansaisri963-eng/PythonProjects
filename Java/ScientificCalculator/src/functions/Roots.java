package functions;

public class Roots {


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


    // ==========================
    // nth Root
    // ==========================

    public static double root(
            double x,
            double n
    ) {

        if (n == 0) {
            throw new ArithmeticException(
                "Zeroth root is undefined"
            );
        }

        if (x < 0 && n % 2 == 0) {
            throw new ArithmeticException(
                "Even root of negative number is undefined"
            );
        }

        return Math.pow(
                x,
                1.0 / n
        );
    }


    // ==========================
    // Reciprocal
    // ==========================

    public static double reciprocal(
            double x
    ) {

        if (x == 0) {
            throw new ArithmeticException(
                "Division by zero"
            );
        }

        return 1.0 / x;
    }

}

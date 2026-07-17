package functions;

public class Logarithms {


    // ==========================
    // Natural Logarithm
    // ==========================

    public static double ln(
            double x
    ) {

        if (x <= 0) {
            throw new ArithmeticException(
                "Natural logarithm undefined for non-positive numbers"
            );
        }

        return Math.log(x);
    }


    // ==========================
    // Base-10 Logarithm
    // ==========================

    public static double log(
            double x
    ) {

        if (x <= 0) {
            throw new ArithmeticException(
                "Logarithm undefined for non-positive numbers"
            );
        }

        return Math.log10(x);
    }


    // ==========================
    // Logarithm with Base
    // ==========================

    public static double log(
            double x,
            double base
    ) {

        if (x <= 0) {
            throw new ArithmeticException(
                "Logarithm undefined for non-positive numbers"
            );
        }

        if (base <= 0 || base == 1) {
            throw new ArithmeticException(
                "Invalid logarithm base"
            );
        }

        return Math.log(x) / Math.log(base);
    }

}

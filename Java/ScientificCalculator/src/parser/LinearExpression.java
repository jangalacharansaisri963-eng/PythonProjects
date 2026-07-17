package parser;

/*
 * Represents a first-degree expression:
 *
 * ax + b
 *
 * Example:
 *
 * 3x + 5
 *
 * coefficient = 3
 * constant = 5
 */

public class LinearExpression {

    private double coefficient;
    private double constant;


    // ==========================
    // Constructors
    // ==========================

    public LinearExpression() {

        coefficient = 0;
        constant = 0;

    }


    public LinearExpression(
            double coefficient,
            double constant
    ) {

        this.coefficient = coefficient;
        this.constant = constant;

    }


    // ==========================
    // Getters
    // ==========================

    public double getCoefficient() {
        return coefficient;
    }


    public double getConstant() {
        return constant;
    }


    // ==========================
    // Setters
    // ==========================

    public void setCoefficient(
            double coefficient
    ) {
        this.coefficient = coefficient;
    }


    public void setConstant(
            double constant
    ) {
        this.constant = constant;
    }


    // ==========================
    // Add
    // ==========================

    public LinearExpression add(
            LinearExpression other
    ) {

        return new LinearExpression(

                this.coefficient + other.coefficient,
                this.constant + other.constant

        );

    }


    // ==========================
    // Subtract
    // ==========================

    public LinearExpression subtract(
            LinearExpression other
    ) {

        return new LinearExpression(

                this.coefficient - other.coefficient,
                this.constant - other.constant

        );

    }


    // ==========================
    // Multiply by Constant
    // ==========================

    public LinearExpression multiply(
            double value
    ) {

        return new LinearExpression(

                coefficient * value,
                constant * value

        );

    }


    // ==========================
    // Negate
    // ==========================

    public LinearExpression negate() {

        return new LinearExpression(

                -coefficient,
                -constant

        );

    }


    // ==========================
    // Is Constant
    // ==========================

    public boolean isConstant() {

        return coefficient == 0;

    }


    // ==========================
    // Is Variable
    // ==========================

    public boolean hasVariable() {

        return coefficient != 0;

    }


    // ==========================
    // toString
    // ==========================

    @Override
    public String toString() {

        return coefficient + "x + " + constant;

    }

}

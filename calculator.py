import sympy as sp
import math

x = sp.symbols("x")

BANNER = """
🐉 Advanced Python Calculator
----------------------------
Supports:
+ - * /
powers (**)
sqrt()
sin()
cos()
tan()
diff <expression>
integrate <expression>
solve <equation>
simplify <expression>

Type 'help' for commands
Type 'exit' to quit
"""

print(BANNER)


def calculate(expr):
    try:
        result = sp.sympify(
            expr,
            locals={
                "sqrt": sp.sqrt,
                "sin": sp.sin,
                "cos": sp.cos,
                "tan": sp.tan,
                "pi": sp.pi
            }
        )

        return sp.simplify(result)

    except Exception:
        return "❌ Invalid expression"


def main():
    while True:
        command = input("\nMath > ").strip()

        if command.lower() == "exit":
            print("Calculator closed.")
            break

        elif command.lower() == "help":
            print(BANNER)

        elif command.startswith("diff "):
            expr = calculate(command[5:])
            print("Derivative:", sp.diff(expr, x))

        elif command.startswith("integrate "):
            expr = calculate(command[10:])
            print("Integral:", sp.integrate(expr, x))

        elif command.startswith("solve "):
            expr = calculate(command[6:])
            print("Solution:", sp.solve(expr, x))

        elif command.startswith("simplify "):
            expr = calculate(command[9:])
            print("Simplified:", sp.simplify(expr))

        else:
            print("Answer:", calculate(command))


if __name__ == "__main__":
    main()

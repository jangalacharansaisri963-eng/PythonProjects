import os
import re
import math
from decimal import Decimal, getcontext
from fractions import Fraction

# ==========================
# ENGINE SETUP
# ==========================

getcontext().prec = 15

DEGREE_MODE = True

# ==========================
# HIGH PRECISION PI
# ==========================

def get_pi():
    old = getcontext().prec
    getcontext().prec += 5

    three = Decimal(3)
    last = Decimal(0)
    t = three
    n = Decimal(1)
    na = Decimal(0)
    d = Decimal(0)
    da = Decimal(24)

    while t != last:
        last = t
        n += na
        na += 8
        d += da
        da += 32
        t += n / d

    getcontext().prec = old
    return +t

PI = get_pi()

# ==========================
# PARSER
# ==========================

def inject_implicit_mul(expr):

    expr = expr.replace("^", "**")

    expr = re.sub(r'(\d)\(', r'\1*(', expr)
    expr = re.sub(r'\)\(', r')*(', expr)

    expr = re.sub(r'(\d)pi', r'\1*pi', expr)
    expr = re.sub(r'pi\(', r'pi*(', expr)

    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)

    return expr

# ==========================
# ANGLES
# ==========================

def to_radians(x):
    if DEGREE_MODE:
        return math.radians(float(x))
    return float(x)

def from_radians(x):
    if DEGREE_MODE:
        return math.degrees(x)
    return x

# ==========================
# TRIG
# ==========================

def sin(x):
    return Decimal(str(math.sin(to_radians(x))))

def cos(x):
    return Decimal(str(math.cos(to_radians(x))))

def tan(x):
    return Decimal(str(math.tan(to_radians(x))))

def asin(x):
    return Decimal(str(from_radians(math.asin(float(x)))))

def acos(x):
    return Decimal(str(from_radians(math.acos(float(x)))))

def atan(x):
    return Decimal(str(from_radians(math.atan(float(x)))))

# ==========================
# HYPERBOLIC
# ==========================

def sinh(x):
    return Decimal(str(math.sinh(float(x))))

def cosh(x):
    return Decimal(str(math.cosh(float(x))))

def tanh(x):
    return Decimal(str(math.tanh(float(x))))

# ==========================
# ROOTS
# ==========================

def sqrt(x):
    return Decimal(str(x)).sqrt()

def cbrt(x):
    return Decimal(str(x)) ** (Decimal(1) / Decimal(3))

def root(n, x):
    return Decimal(str(x)) ** (Decimal(1) / Decimal(n))

# ==========================
# LOGS
# ==========================

def ln(x):
    return Decimal(str(math.log(float(x))))

def log(x):
    return Decimal(str(math.log10(float(x))))

# ==========================
# FACTORIAL
# ==========================

def factorial(x):
    return math.factorial(int(x))

# ==========================
# FIND RATIONALS
# ==========================

def fr(a, b, count):

    a = Fraction(str(a))
    b = Fraction(str(b))

    if a > b:
        a, b = b, a

    found = []
    denom = 1

    while len(found) < count:

        for numer in range(
            math.floor(float(a * denom)) + 1,
            math.ceil(float(b * denom))
        ):

            f = Fraction(numer, denom)

            if a < f < b and f not in found:
                found.append(f)

                if len(found) >= count:
                    break

        denom += 1

    found.sort()

    print("\n━━━━━━━━━━━━━━━━━━━━━━")

    print(f"{count} Rational Numbers")

    print(f"Between {float(a)} and {float(b)}")

    print("━━━━━━━━━━━━━━━━━━━━━━")

    for f in found:
        print(f"{f} = {float(f)}")

    print("━━━━━━━━━━━━━━━━━━━━━━")

# ==========================
# LIBRARY
# ==========================

MATH_LIB = {

    "sin": sin,
    "cos": cos,
    "tan": tan,

    "asin": asin,
    "acos": acos,
    "atan": atan,

    "sinh": sinh,
    "cosh": cosh,
    "tanh": tanh,

    "sqrt": sqrt,
    "cbrt": cbrt,
    "root": root,

    "ln": ln,
    "log": log,

    "factorial": factorial,

    "Decimal": Decimal,

    "pi": PI
}

# ==========================
# TERMINAL
# ==========================

def run_calculator():

    global DEGREE_MODE

    print("===================================")
    print(" High Precision Scientific Calculator")
    print("===================================")
    print("Type 'exit' to quit.")
    print("Add 'precise' to any calculation for 105-digit precision.")
    print("Commands:")
    print("  mode degree")
    print("  mode radian")
    print("  fr(a,b) n")
    print()

    while True:

        cmd = input("calc:~$ ").strip()

        if not cmd:
            continue

        if cmd.lower() in ("exit", "quit"):
            break

        if cmd.lower() in ("clear", "cls"):
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if cmd.lower() == "mode degree":
            DEGREE_MODE = True
            print(">> Degree mode enabled.")
            continue

        if cmd.lower() == "mode radian":
            DEGREE_MODE = False
            print(">> Radian mode enabled.")
            continue

        # -------------------------
        # Precision Toggle
        # -------------------------

        precise = False

        if cmd.lower().endswith(" precise"):
            precise = True
            cmd = cmd[:-8].strip()
            getcontext().prec = 105
        else:
            getcontext().prec = 15

        # Refresh pi if precision changed
        global PI
        PI = get_pi()
        MATH_LIB["pi"] = PI

        # -------------------------
        # Find Rational Numbers
        # -------------------------

        fr_match = re.fullmatch(
            r'fr\s*\(\s*([^,]+)\s*,\s*([^)]+)\s*\)\s*(\d+)',
            cmd
        )

        if fr_match:

            try:

                left = eval(
                    inject_implicit_mul(fr_match.group(1)),
                    {"__builtins__": None},
                    MATH_LIB
                )

                right = eval(
                    inject_implicit_mul(fr_match.group(2)),
                    {"__builtins__": None},
                    MATH_LIB
                )

                amount = int(fr_match.group(3))

                fr(left, right, amount)

            except Exception as e:
                print("Error:", e)

            continue

        # -------------------------
        # Normal Evaluation
        # -------------------------

        try:

            expression = inject_implicit_mul(cmd)

            result = eval(
                expression,
                {"__builtins__": None},
                MATH_LIB
            )

            print()
            print("━━━━━━━━━━━━━━━━━━━━━━")
            print("Result")
            print("━━━━━━━━━━━━━━━━━━━━━━")

            print(result)

            if precise:
                print("(Precise Mode)")

            print("━━━━━━━━━━━━━━━━━━━━━━")
            print()

        except ZeroDivisionError:
            print("Error: Division by zero.")

        except OverflowError:
            print("Error: Number too large.")

        except ValueError:
            print("Error: Invalid mathematical operation.")

        except Exception as e:
            print("Error:", e)


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":
    run_calculator()
    

import os
import re
import cmath
import math
from decimal import Decimal, getcontext

# --- ENGINE SETUP ---
# Default to 15 for speed, 105 for when you add "precise"
getcontext().prec = 15 

def inject_implicit_mul(expr):
    expr = re.sub(r'(\d)\(', r'\1*(', expr)
    expr = re.sub(r'\)\(', r')*(', expr)
    expr = re.sub(r'(\d)([a-z])', r'\1*\2', expr)
    return expr

def get_high_precision_pi():
    orig_prec = getcontext().prec
    getcontext().prec = 110
    C = 426880 * Decimal(10005).sqrt()
    M, L, X, K, S = 1, 13591409, 1, 6, 13591409
    for i in range(1, 3):
        M = (M * (K**3 - 16*K)) // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi_val = C / S
    getcontext().prec = orig_prec
    return pi_val

def get_high_precision_e():
    e = Decimal(1); fact = Decimal(1)
    for i in range(1, 70): fact *= Decimal(i); e += Decimal(1) / fact
    return e

# --- YOUR MATH SUITE ---
def smart_sin(deg):
    x = (Decimal(deg) * get_high_precision_pi() / Decimal(180)) % (2 * get_high_precision_pi())
    result, term, num, denom, sign = Decimal(0), x, x, 1, 1
    for i in range(1, 45):
        result += sign * term; num *= x * x; denom *= (2 * i) * (2 * i + 1)
        term = num / Decimal(denom); sign *= -1
    return result

def smart_cos(deg):
    x = (Decimal(deg) * get_high_precision_pi() / Decimal(180)) % (2 * get_high_precision_pi())
    result, term, num, denom, sign = Decimal(0), Decimal(1), Decimal(1), 1, 1
    for i in range(1, 45):
        result += sign * term; num *= x * x; denom *= (2 * i - 1) * (2 * i)
        term = num / Decimal(denom); sign *= -1
    return result

def smart_tan(deg): return smart_sin(deg) / smart_cos(deg)
def smart_sqrt(x): return Decimal(x).sqrt()
def smart_log(x): return Decimal(math.log10(float(x)))
def smart_ln(x):
    x = Decimal(x); res = Decimal(str(cmath.log(float(x)).real)); e = get_high_precision_e()
    for _ in range(7): res = res + (x / (e ** res)) - Decimal(1)
    return res

def find_repeating_decimal(n, d):
    num, den = int(n), int(d)
    integer_part = num // den
    remainder = num % den
    if remainder == 0: return f"{integer_part}.0"
    decimal_part, seen = [], {}
    while remainder != 0 and len(decimal_part) < 102:
        if remainder in seen: break
        seen[remainder] = len(decimal_part)
        remainder *= 10; decimal_part.append(str(remainder // den)); remainder %= den
    return f"{integer_part}.{''.join(decimal_part)}"

# --- MAIN LOOP ---
def run_calculator():
    print("--- High-Precision Scientific Calculator ---")
    
    MATH_LIB = {
        "sin": smart_sin, "cos": smart_cos, "tan": smart_tan,
        "pi": get_high_precision_pi(), "ln": smart_ln, "log": smart_log,
        "sqrt": smart_sqrt, "Decimal": Decimal
    }
    
    while True:
        cmd = input("calc:~$ ").strip()
        if cmd.lower() in ["exit", "quit"]: break
        if cmd.lower() in ["clear", "cls"]:
            os.system('cls' if os.name == 'nt' else 'clear'); continue
            
        # Toggle Precision
        is_precise = cmd.lower().endswith(" precise")
        if is_precise:
            getcontext().prec = 105
            cmd = cmd.replace(" precise", "").strip()
        else:
            getcontext().prec = 15

        try:
            # Handle fr(a,b) count
            fr_match = re.match(r'fr\((\d+),(\d+)\)\s+(\d+)', cmd)
            if fr_match:
                n, d, count = fr_match.groups()
                # Your specific logic for fr range goes here
                print("Result: [Rational Sequence]")
            else:
                result = eval(inject_implicit_mul(cmd), {"__builtins__": None}, MATH_LIB)
                print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_calculator()
    

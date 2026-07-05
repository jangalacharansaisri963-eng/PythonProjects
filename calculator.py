import math
import os
import re

def clear_screen():
    """Clears the terminal screen for Windows or Linux/Android."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print("--- Professional Calculator ---")
    print("Features: +, -, *, /, sqrt(x), cbrt(x), pi(n), pi, pow(x, y), percent(x, y), sin(x), cos(x), tan(x), radians(x), degrees(x)")
    print("Commands: 'ans' (last result), 'clear' (wipe screen), 'exit' (close)")
    
    # Initialize the Ans memory buffer tracker
    ans_value = 0

    # Custom helper for percentage calculations
    def percent(x, y):
        return (x / 100) * y

    # Custom helper for pi with specified decimal precision: pi(n)
    def pi_precision(n):
        return round(math.pi, int(n))

    # Smart trig functions to cleanly handle floating-point rounding artifacts
    def smart_sin(x):
        res = math.sin(x)
        return 0 if math.isclose(res, 0, abs_tol=1e-15) else res

    def smart_cos(x):
        res = math.cos(x)
        return 0 if math.isclose(res, 0, abs_tol=1e-15) else res

    def smart_tan(x):
        cosine = smart_cos(x)
        if cosine == 0:
            raise ValueError("Undefined (Tangent asymptote)")
        res = math.tan(x)
        return 0 if math.isclose(res, 0, abs_tol=1e-15) else res

    # The namespace dictionary mapping string inputs to safe math entities
    safe_dict = {
        "sqrt": math.sqrt,
        "cbrt": math.cbrt,      
        "pi": pi_precision,     
        "pow": math.pow,      
        "percent": percent,    
        "sin": smart_sin,      
        "cos": smart_cos,      
        "tan": smart_tan,      
        "radians": math.radians,
        "degrees": math.degrees 
    }

    while True:
        try:
            expr = input("\n> ").lower().strip()
            
            # Handle exit conditions
            if expr in ["exit", "quit"]:
                print("Goodbye!")
                break
                
            # Handle an empty input gracefully
            if not expr:
                continue

            # Handle screen clear command
            if expr in ["clear", "cls"]:
                clear_screen()
                continue

            # --- BUFF 1: Replace 'ans' with the actual stored memory value ---
            expr = re.sub(r'\bans\b', str(ans_value), expr)

            # Special Case: If user types just 'pi' without brackets, return raw representation
            if expr == "pi":
                result = math.pi
                print(f"= {format(result, '.30f')}")
                ans_value = result  # Update ans even for raw pi calls
                continue

            # --- BUFF 2: Smart Implicit Multiplication Injector ---
            # Fixes number touching open bracket: 2(3) -> 2*(3)
            expr = re.sub(r'(\d)\(', r'\1*(', expr)
            # Fixes closing bracket touching open bracket: (2)(3) -> (2)*(3)
            expr = re.sub(r'\)\(', r')*(', expr)
            # Fixes number touching a math word/constant: 2pi -> 2*pi or 2sqrt(4) -> 2*sqrt(4)
            expr = re.sub(r'(\d)([a-z])', r'\1*\2', expr)

            # Build a local dictionary where 'pi' acts as a static constant value
            local_dict = {"pi": math.pi}
            
            # Safe parsing execution context
            result = eval(expr, {"__builtins__": None}, {**safe_dict, **local_dict})
            
            # Clean up outputs (stripping floating point artifacts like -0 or .0)
            if isinstance(result, (int, float)):
                if math.isclose(result, 0, abs_tol=1e-15):
                    result = 0
                elif result.is_integer():
                    result = int(result)

            print(f"= {result}")
            
            # Save final successful calculation back into the Ans buffer
            ans_value = result
            
        except ZeroDivisionError:
            print("Undefined")
        except NameError:
            print("Error: Unknown function or variable used.")
        except TypeError:
            print("Error: Invalid argument layout or missing brackets.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            # Check if eval blew up specifically due to a hidden division by zero in float math
            if "division by zero" in str(e).lower():
                print("Undefined")
            else:
                print(f"Error: Invalid syntax.")

if __name__ == "__main__":
    calculator()
    

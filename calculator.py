import math

def calculator():
    print("--- Professional Calculator ---")
    print("Features: +, -, *, /, sqrt(x), cbrt(x), pi(n), pi, pow(x, y), percent(x, y), sin(x), cos(x), tan(x), radians(x), degrees(x)")
    print("Type 'exit' or 'quit' to close.")
    
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
        "cbrt": math.cbrt,      # <-- Added cube root support here!
        "pi": pi_precision,     # Used when called as a function: pi(5)
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

            # Special Case: If user types just 'pi' without brackets, return raw 30-digit float representation
            if expr == "pi":
                print(f"= {format(math.pi, '.30f')}")
                continue

            # Build a local dictionary where 'pi' as a word acts as a constant value for equations like '2 * pi'
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
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except NameError:
            print("Error: Unknown function or variable used.")
        except TypeError:
            print("Error: Invalid argument layout or missing brackets.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: Invalid syntax.")

if __name__ == "__main__":
    calculator()
    

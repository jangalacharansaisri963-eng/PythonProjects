import math

def calculator():
    print("--- Professional Calculator ---")
    print("Features: +, -, *, /, sqrt(x), pi(n), pi, pow(x, y), percent(x, y), sin(x), cos(x), tan(x), radians(x), degrees(x)")
    print("Type 'exit' or 'quit' to close.")
    
    # Custom operations
    def percent(x, y):
        return (x / 100) * y

    # Smart pi function that works as a constant OR a function: pi(5)
    class SmartPi:
        def __call__(self, n=None):
            if n is None:
                return math.pi
            return round(math.pi, int(n))
        
        # Allows regular 'pi + 2' math expressions to work without brackets
        def __radd__(self, other): return other + math.pi
        def __add__(self, other): return math.pi + other
        def __rsub__(self, other): return other - math.pi
        def __sub__(self, other): return math.pi - other
        def __rmul__(self, other): return other * math.pi
        def __mul__(self, other): return math.pi * other
        def __rtruediv__(self, other): return other / math.pi
        def __truediv__(self, other): return math.pi / other
        def __repr__(self): return format(math.pi, '.30f')

    safe_dict = {
        "sqrt": math.sqrt,
        "pi": SmartPi(),       # Handles both 'pi' and 'pi(n)'
        "pow": math.pow,      
        "percent": percent,    
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "radians": math.radians,
        "degrees": math.degrees # <-- Added degrees here!
    }

    while True:
        try:
            expr = input("\n> ").lower().strip()
            
            if expr in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            # Evaluate expression safely
            result = eval(expr, {"__builtins__": None}, safe_dict)
            
            # If result is a float, cleanly print it; otherwise let SmartPi handle its string representation
            if isinstance(result, float) and result.is_integer():
                print(f"= {int(result)}")
            else:
                print(f"= {result}")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except NameError as e:
            print(f"Error: Unknown function or variable used.")
        except TypeError as e:
            print(f"Error: Invalid argument type or missing brackets.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
    

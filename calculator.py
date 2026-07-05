def calculator():
    print("--- Simple Python Calculator ---")
    print("Options: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+': print(f"Result: {num1 + num2}")
            elif op == '-': print(f"Result: {num1 - num2}")
            elif op == '*': print(f"Result: {num1 * num2}")
            elif op == '/':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
            else:
                print("Invalid operator!")
                
            again = input("Do another? (y/n): ")
            if again.lower() != 'y':
                break
        except ValueError:
            print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    calculator()
    

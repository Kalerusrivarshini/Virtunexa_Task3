
def calculator():
    try:
        expr = input("Enter expression (e.g., 2 + 2): ")
        result = eval(expr)
        print("Result:", result)
        with open("logs/calc_history.txt", "a") as f:
            f.write(f"{expr} = {result}\n")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("Invalid input:", e)

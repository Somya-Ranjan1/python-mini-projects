print("Calculator")

while True:
    try:
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Second number: "))
        operator = input("Enter operator (+, -, *, /, %): ")

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero not allowed")
            else:
                print("Result:", num1 / num2)

        elif operator == "%":
            print("Result:", num1 % num2)

        else:
            print("Invalid operator!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        print("Calculator stopped.")
        break
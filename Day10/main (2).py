def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = num1 + num2
            operator = "+"
        elif choice == "2":
            result = num1 - num2
            operator = "-"
        elif choice == "3":
            result = num1 * num2
            operator = "*"
        else:
            if num2 != 0:
                result = num1 / num2
                operator = "/"
            else:
                print("Error: Cannot divide by zero!")
                return

        print("Result:", num1, operator, num2, "=", result)
    else:
        print("Invalid choice!")

calculator()

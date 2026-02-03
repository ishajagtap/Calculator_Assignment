from .add import add
from .subtract import subtract
from .multiply import multiply
from .divide import divide



def main():
    print("Simple Calculator")
    print("-----------------")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
        print("Result:", result)

    elif choice == "2":
        result = subtract(a, b)
        print("Result:", result)

    elif choice == "3":
        result = multiply(a, b)
        print("Result:", result)

    elif choice == "4":
        try:
            result = divide(a, b)
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid choice")
    


if __name__ == "__main__":
    main()

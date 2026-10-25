class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Oops! You can't divide by zero."
        return a / b

def main():
    calc = Calculator()
    
    print("Hey there! Let's do some math.")
    
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("That doesn't look like a number. Try again!")
        return

    print("\nWhat would you like to do?")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Pick a number (1-4): ")

    if choice == '1':
        print(f"Total: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc.multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {calc.divide(num1, num2)}")
    else:
        print("That wasn't an option, sorry!")

if __name__ == "__main__":
    main()

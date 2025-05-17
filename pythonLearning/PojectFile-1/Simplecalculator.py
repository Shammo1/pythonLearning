def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> int:
    return x // y  

def modulo(x: int, y: int) -> int:
    return x % y

print("Enter Two Numbers:")
a = int(input("First number: "))
b = int(input("Second number: "))

print("\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Modulo (%)\n")
choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    print(f"Result: {add(a, b)}")
elif choice == 2:
    print(f"Result: {subtract(a, b)}")
elif choice == 3:
    print(f"Result: {multiply(a, b)}")
elif choice == 4:
    if b == 0:
        print("Error: Division by zero!")
    else:
        print(f"Result: {divide(a, b)}")
elif choice == 5:
    if b == 0:
        print("Error: Modulo by zero!")
    else:
        print(f"Result: {modulo(a, b)}")
else:
    print("Invalid choice! Please enter 1-5.")
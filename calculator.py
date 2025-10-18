# Simple Calculator in Python

print(" Simple Calculator ")

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Taking user's choice
choice = input("Enter your choice (1/2/3/4): ")

# Performing calculation based on user's choice
if choice == '1':
    result = num1 + num2
    print(f"\n The result is: {result}")

elif choice == '2':
    result = num1 - num2
    print(f"\n The result is: {result}")

elif choice == '3':
    result = num1 * num2
    print(f"\n The result is: {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\n The result is: {result}")
    else:
        print("\n Error! Division by zero is not allowed.")

else:
    print("\n Invalid choice! Please select 1, 2, 3, or 4.")
    
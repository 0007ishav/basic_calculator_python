def add(a , b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def exponential(a, b):
    return a ** b

print("Select your operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponential")

while True:
    choice = input("Enter your choice(1/2/3/4/5/6): ")

    if choice in ('1','2','3','4','5','6'):
        try:
            a = float(input("Enter you first value: "))
            b = float(input("Enter you second value: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print('The sum of',a,'and', b,'is =', add(a, b))

        elif choice == '2':
            print('The subtraction of',a,'and', b,'is =', subtract(a, b))

        elif choice == '3':
            print('The multiplication of',a,'and', b,'is =', multiply(a, b))

        elif choice == '4':
            print('The division of',a,'and', b,'is =', divide(a, b))

        elif choice == '5':
            print('The modulus of',a,'and', b,'is =', modulus(a, b))

        elif choice == '6':
            print('The exponential of',a,'and', b,'is =', exponential(a, b))


        # Check if user wants another calculation
        # Then break the loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no" or next_calculation == "n":
            break
    else:
        print("Invalid choice")



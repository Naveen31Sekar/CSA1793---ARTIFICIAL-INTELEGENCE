def calculator():
    while True:
        print("Enter 'quit' to exit")
        num1 = input("Enter a number: ")
        if num1 == 'quit':
            break
        num2 = input("Enter another number: ")
        if num2 == 'quit':
            break
        operation = input("Enter an operation (+,-,*,/): ")
        if operation == 'quit':
            break
        if operation == '+':
            print(float(num1) + float(num2))
        elif operation == '-':
            print(float(num1) - float(num2))
        elif operation == '*':
            print(float(num1) * float(num2))
        elif operation == '/':
            print(float(num1) / float(num2))
        else:
            print("Invalid operator")

calculator()

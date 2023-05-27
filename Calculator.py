def sum(x: int, y: int) -> int:
    return x + y


def reduce(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> int:
    return x / y


print('--Welcome to the calculator--')

while True:
    print('1 +')
    print('2 -')
    print('3 x')
    print('4 /')
    print('5 exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(sum(num1, num2))
    elif choice == '2':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(reduce(num1, num2))
    elif choice == '3':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(multiply(num1, num2))
    elif choice == '4':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(divide(num1, num2))
    elif choice == '5':
        break
    else:
        print('Invalid choice')

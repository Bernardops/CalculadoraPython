import math


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y


def power(x, y):
    return x ** y


def root(x, y):
    if x < 0 and y % 2 == 0:
        return "Erro! Raiz de número negativo."
    return x ** (1 / y)


def factorial(x):
    if x < 0:
        return "Erro! Fatorial de número negativo."
    return math.factorial(x)


def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Radiciação")
    print("7. Fatorial")

    while True:
        choice = input("Digite sua escolha (1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {addition(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {division(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")
                elif choice == '6':
                    print(f"{num1} raíz de {num2} = {root(num1, num2)}")
            except ValueError:
                print("Erro! Por favor, insira um número válido.")

        elif choice == '7':
            try:
                num = int(input("Digite um número inteiro: "))
                print(f"{num}! = {factorial(num)}")
            except ValueError:
                print("Erro! Por favor, insira um número inteiro válido.")

        else:
            print("Opção inválida!")
            continue

        next_calculation = input("Deseja realizar outra operação? (s/n): ")
        if next_calculation.lower() != 's':
            break


calculator()

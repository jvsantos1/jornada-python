# Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    temp_fahrenheit = temp_celsius * 1.8 + 32
    print(f"A temperatura em Fahrenheit é: {temp_fahrenheit}")
except:
    print("O valor informado precisa ser um número!")

# Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
try:
    palindromo = input("Digite uma palavra: ")
    if isinstance(palindromo, str):
        palindromo = palindromo.replace(" ", "").lower()
        if palindromo == palindromo[::-1]:
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo!")
except:
    print("Entrada inválida! Digite apenas letras.")

# Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        print(f"Resultado: {num1 + num2}")
    elif operador == "-":
        print(f"Resultado: {num1 - num2}")
    elif operador == "*":
        print(f"Resultado: {num1 * num2}")
    elif operador == "/":
        if num2 == 0:
            print("Divisão por zero!")
        else:
            print(f"Resultado: {num1 / num2}")
    else:
        print("Operador inválido!")
except:
    print("Entrada inválida! Digite apenas números.")

# Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    num = float(input("Digite um número: "))
    if num > 0:
        print("Positivo!")
    elif num < 0:
        print("Negativo!")
    else:
        print("Zero!")
    if num % 2 == 0:
        print("Par!")
    else:
        print("Ímpar!")
except:
    print("Entrada inválida! Digite apenas números.")

# Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
list_num = input("Digite uma lista de números separados por vírgula: ").split(",")
for num in list_num:
    try:
        num = int(num)
        print(num)
    except:
        print("Entrada inválida! Digite apenas números.")

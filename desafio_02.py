### Desafio - Refatorar o projeto do desafio anterior evitando Bugs!
# 1) Solicita ao usuário que digite seu nome
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")

if nome.isdigit() or nome == "" or nome.isspace():
    print("Nome inválido!")
    exit()

try:
    salario = float(input("Digite seu salario: ").replace(",", "."))
    bônus = float(input("Digite seu bônus: ").replace(",", "."))
    if salario < 0 or bônus < 0:
        print("Valor de salário ou bônus inválido!")
        exit()
    calc_kpi = CONSTANTE_BONUS + float(salario) * float(bônus)
except:
    print("Valor de salário ou bônus inválido!")
    exit()

print(
    f"Olá {nome} o valor do seu salário é {float(salario)} reais e seu bonus foi de {float(bônus)} reais e o seu kpi é de {calc_kpi} reais"
)

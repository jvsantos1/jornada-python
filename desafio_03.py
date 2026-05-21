# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

CONSTANTE_BONUS: int = 1000
validacao: bool = True

# Solicita ao usuário que digite seu nome

while validacao:
    try:
        nome: str = input("Digite seu nome: ")
        if nome.isdigit() or nome == "" or nome.isspace():
            print("Nome inválido! Digite um nome válido")
        else: break
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
while validacao:
    try:
        salario: float = float(input("Digite seu salario: ").replace(",", "."))
        if salario < 0:
            print("Valor do salário inválido! Digite um valor válido")
        else: break
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while validacao:
    try:
        bonus: float = float(input("Digite seu bônus: ").replace(",", "."))
        if bonus < 0:
            print("Valor do bônus inválido! Digite novamente")
        else: break
    except ValueError as e:
        print(e)

# Imprime as informações para o usuário
calc_kpi: float = CONSTANTE_BONUS + salario * bonus
print(
    f"Olá {nome} o valor do seu salário é {float(salario)} reais e seu bonus foi de {float(bonus)} reais e o seu kpi é de {float(calc_kpi)} reais"
)
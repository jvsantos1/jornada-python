# Desafio do dia: Cálculo de Bônus com Entrada do Usuário

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
# Regra de calculo de KPI: 1000 + salario * bonus


CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")
salario = input("Digite seu salario: ").replace(",", ".")
bônus = input("Digite seu bônus: ").replace(",", ".")

calc_kpi = CONSTANTE_BONUS + float(salario) * float(bônus)

print(
    f"Olá {nome} o valor do seu salário é {float(salario)} reais e seu bonus foi de {float(bônus)} reais e o seu kpi é de {calc_kpi} reais"
)

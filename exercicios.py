# Exercício Bônus Salarial com variaveis de erro:

VALOR_FIXO_BONUS = 1000

nome_usuario = input("Digite seu nome: ")

if nome_usuario.isdigit():
    print("Voce digitou seu nome errado")
    exit()
elif nome_usuario.isspace():
    print("Voce apenas digitou espaço")
    exit()
elif len(nome_usuario) == 0:
    print("Voce não digitou nada")
    exit()

salario_usuario = float(input("Digite seu salário: "))

if salario_usuario < 1000:
    print("Você digitou seu salário errado")
    exit()

bonus_usuario = float(input("Digite seu bônus: "))

if bonus_usuario < 0 or bonus_usuario > 1:
    print("Bonus pode apenas ser entre 0 a 1. EX: 30% = 0.30")
    exit()


valor_bonus = VALOR_FIXO_BONUS + salario_usuario * bonus_usuario
print(f"O usuário {nome_usuario} possui o bonus de {valor_bonus}")
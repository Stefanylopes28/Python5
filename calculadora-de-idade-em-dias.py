from datetime import datetime

def calcular_idade_em_dias():
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento (AAAA): "))
        ano_atual = datetime.now().year

        idade = ano_atual - ano_nascimento
        idade_em_dias = idade * 365  # Aproximação simples, como solicitado

        print(f"Sua idade aproximada em dias é: {idade_em_dias} dias.")
    except ValueError:
        print("Por favor, insira um ano válido.")

calcular_idade_em_dias()
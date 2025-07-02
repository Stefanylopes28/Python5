def calcular_gorjeta():
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta que deseja deixar: "))

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    print(f"A gorjeta a ser deixada é: R$ {gorjeta:.2f}")

calcular_gorjeta()

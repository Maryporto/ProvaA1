def binario_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        digito = int(binario[i])
        decimal += digito * (2 ** (len(binario) - 1 - i))
    return decimal

binario = input("Digite um número binário: ")
print("O número binário", binario, "em decimal é:", binario_decimal(binario))

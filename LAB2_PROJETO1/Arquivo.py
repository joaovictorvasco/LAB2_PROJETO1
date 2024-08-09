import random as rd

def cumprimento(texto):
    return f"Olá, {texto}"

print(cumprimento("João Victor Sepulveda Penido"))

def sorteia_media():
    numeros = [rd.randint(1, 100) for _ in range(3)]
    media = sum(numeros) / 3
    return media

print(f"A média dos três números sorteados é: {sorteia_media()}")

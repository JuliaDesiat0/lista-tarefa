vetA = "COMPUTACAO"
vetB = input("Digite uma palavra de 10 letras: ")

for i, letra in enumerate(vetB):
    if letra.upper() == vetA[i].upper():
        print(i, end=" ")


string = input("Digite uma string: ")
print("A string digitada foi:", string)

comprimento = len(string)
print("O comprimento da string é:", comprimento)

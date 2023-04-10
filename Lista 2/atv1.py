palavra = input("Digite uma palavra de no máximo 10 caracteres: ")
vogais = 0

for c in palavra:
    if c in "aeiouAEIOU":
        vogais += 1

print(f"A palavra {palavra} tem {vogais} vogais.")

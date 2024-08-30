def cont_letra(palavra: str) -> int:
    cont = 0
    for letra in palavra:
        if letra.lower() == 'a':
            cont += 1
    return cont

palavra = input("Insira a palavra em que deseja procurar a letra 'A': ")
print(f"Foram encontradas {cont_letra(palavra)} letras A na palavra '{palavra}'")

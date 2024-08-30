def is_fibonacci(n: int)-> bool:
    if n < 0:
        return False
    lista = [0, 1]

    i = 0
    while lista[i + 1] < n:
        lista.append(lista[i] + lista[i + 1])
        if n in lista:
            return True
        i += 1
    return False


print(is_fibonacci(int(input('Insira o número a ser verificado: '))))
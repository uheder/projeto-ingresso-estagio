def is_fibonacci(n: int)-> bool:
    if n < 0:
        return False
    lista = [0, 1]
    
    if n == 0 or n == 1:
        return "É um número da sequência Fibonacci"
    i = 0
    while lista[i + 1] < n:
        lista.append(lista[i] + lista[i + 1])
        if n in lista:
            return "É um número da sequência Fibonacci"
        i += 1
    return "Não é um número da sequência Fibonacci"


print(is_fibonacci(int(input('Insira o número a ser verificado: '))))
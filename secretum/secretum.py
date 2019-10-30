#!/bin/python3

"""Methods to decrypt the secretum."""


def decrypt(value):
    """Decrypt iteratiu """
    num = int(value)
    while num > 9:
        aux = num
        sumatori = 0
        while aux:
            sumatori += aux % 10
            aux //= 10
        num = sumatori
    return num


def suma_recursiva(value):
    """Suma recursiva de digits """

    aux = int(value)
    if aux <= 9:
        return aux
    ultimo_digito = aux % 10
    resto = aux // 10
    return ultimo_digito + suma_recursiva(resto)


def decrypt_recursive(value):
    """Decrypt recursio """

    aux = suma_recursiva(value)
    if aux <= 9:
        return aux
    return decrypt_recursive(aux)


def main():
    """Main function to parse input/output
    and decrypt the secretum."""


if __name__ == '__main__':
    main()

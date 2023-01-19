def fatorial(num, show=False):
    """
    => Calcular fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)

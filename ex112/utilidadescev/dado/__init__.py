def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \"{entrada}\" é um preço invalido.')
        else:
            válido = True
            return float(entrada)
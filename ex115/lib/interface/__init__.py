def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, informe um número válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário prefiriu não digitar.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '\033[33m-\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    #Cabeçalho do menu
    cabeçalho('MENU PRINCIPAL')
    #Codigo para apresentar as opções
    c = 1
    for item in lista:
        print(f'\033[34m{c} - {item}\033[m')
        c += 1
    #fim codigo
    print(linha())
    #Codigo para leitura de opções
    opc = leiaint('\033[35mEscolha uma das opções: \033[m')
    return opc
    #fim codigo
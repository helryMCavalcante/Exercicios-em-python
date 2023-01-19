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
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! informa um valor do tipo flutuante.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não informa nenhum valor.\033[m')
            return 0
        else:
            return n
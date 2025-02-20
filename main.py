while True:

    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite um número: ")
    operador = input(
        'Digite o opeador (Adição(+), Subtraçao(-), Multipllicação(*) e Divisão(/))')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2-float = float(numero_2)
        numeros_validos = True

    except Exception as error:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos dos números digitados são invalidos. ')
        continue

    sair = input('Quer sair? [s]im').lower().startswith('s')

    if sair is True:
        break

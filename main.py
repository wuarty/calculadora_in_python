from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

if __name__ == "__main__":
    app = QApplication([])
    main_window = QMainWindow()
    main_window.setWindowTitle("Calculadora")
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)
    main_window.show()
    app.exec()

# while True:

#     numero_1 = input("Digite um número: ")
#     numero_2 = input("Digite um número: ")
#     operador = input(
#         'Digite o opeador (Adição(+), Subtraçao(-), Multipllicação(*) e Divisão(/)): ')

#     numeros_validos = False
#     num_1_float = 0.0
#     num_2_float = 0.0

#     try:
#         num_1_float = float(numero_1)
#         num_2_float = float(numero_2)
#         numeros_validos = True

#     except Exception as error:
#         numeros_validos = None

#     if numeros_validos is None:
#         print('Um ou ambos dos números digitados são invalidos. ')
#         continue

#     operadores_permitidos = '+-/*'

#     if operador not in operadores_permitidos:
#         print('Digite apenas um operador valido')
#         continue

#     if len(operador) > 1:
#         print('Operador inválido ')

#     print('Realizando calculo...')
#     if operador == '+':
#         resultado = num_1_float + num_2_float
#         print(f'O resultado da soma é: {resultado}')
#     elif operador == '-':
#         resultado = num_1_float - num_2_float
#         print(f'O resultado da subtração é: {resultado}')
#     elif operador == '*':
#         resultado = num_1_float * num_2_float
#         print(f'O resultado da multiplicação é: {resultado}')
#     elif operador == '/':
#         resultado = num_1_float / num_2_float
#         print(f'O resultado da divisão é: {resultado}')

#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
    # break

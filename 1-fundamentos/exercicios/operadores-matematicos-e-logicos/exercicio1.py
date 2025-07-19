# Peça dois números e exiba o resultado das quatro operações básicas entre eles.

numero1 = float(input('\nDigite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f'''\nResultados das operações:
        Soma: {soma}
        Subtração: {subtracao}
        Multiplicação: {multiplicacao}
        Divisão: {divisao:.1f}
        ''')
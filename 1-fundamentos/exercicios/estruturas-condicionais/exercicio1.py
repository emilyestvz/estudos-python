# Peça um número e diga se ele é positivo, negativo ou zero.

numero = float(input(f'\nDigite um número: '))

print(f'\nO número digitado foi: {numero}')

if numero > 0:
    print('Este número é positiivo!')
elif numero < 0:
    print('Este número é negativo!')
else:
    print('Este número é um zero!')
    

# Peça uma lista de 5 números (usando `input()` e `split()`) e imprima a soma com `sum()` e o maior número com `max()`.

numeros = input(f'\nDigite 5 números separados por espaço: ').split()

numeros = [int(numero) for numero in numeros]

print(f'\nA soma dos números é: {sum(numeros)}')
print(f'O maior número é: {max(numeros)}\n')

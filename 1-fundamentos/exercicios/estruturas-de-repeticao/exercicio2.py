# Peça um número e exiba a tabuada dele de 1 a 10 usando `while`.

print(f'\n############# TABUADA ##############')
numero = int(input('Digite um número: '))

contador = 1

while contador <= 10:
    resultado = numero * contador
    
    print(f'{numero} x {contador} = {resultado}')
    
    contador += 1
    
print('#####################################\n')
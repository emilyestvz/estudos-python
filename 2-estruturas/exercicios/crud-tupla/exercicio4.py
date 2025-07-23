# 1. Crie uma tupla com 3 cores
# 2. Acesse a segunda cor
# 3. Tente alterar a cor (e veja o que acontece). Coloque o resultado como comentario

cores = ('preto', 'branco', 'violeta')

cor = cores[1]
print(f'A segunda cor é: {cor} ✨')

cores[1] = 'azul'
print(f'Tentando alterar a cor: {cores}')
# Resultado: TypeError: 'tuple' object does not support item assignment
# Tuplas são imutáveis, por isso não é possível alterar seus elementos após sua criação.

# Criar e manipular um set
# 1. Crie um conjunto com 3 nomes de linguagens de programação
# 2. Adicione uma nova linguagem
# 3. Remova uma linguagem
# 4. Verifique se "Python" está no conjunto

# FIX: resoluções simples e sem interface de usuário, apenas operações básicas com sets.

linguagens = {'Python', 'Java', 'C++'}

linguagens.add('Typescript')
print(f'Conjunto de linguagens: {linguagens}')

linguagens.discard('Java')
print(f'Conjunto após remoção: {linguagens}')

if 'Python' in linguagens:
    print('Python está no conjunto.')
else:
    print('Python não está no conjunto.')






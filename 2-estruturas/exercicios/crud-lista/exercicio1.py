# Crie um programa que permita: 
# 1. Adicionar nomes a uma lista. 
# 2. Exibir todos os nomes
# 3. Atualizar um nome existente
# 4. Remover um nome

nomes = []

while True:
    print(f'\n############ MENU ############')
    print(f'''
        1. Adicionar nome
        2. Exibir nomes
        3. Atualizar nome
        4. Remover nome
        5. Sair
          ''')
    
    opcao = int(input('✨ Digite a sua opção: '))
        
    if opcao == 1:
        nome = input('✨ Digite o nome a ser adicionado: ')
        nomes.append(nome)
        
    elif opcao == 2:
        for nome in nomes:
            print(f'- {nome}')
            
    elif opcao == 3:
        nome = input('✨ Digite o nome a ser atualizado: ')
        if nome in nomes:
            nomes.remove(nome)
            nomes.append(input('✨ Digite o novo nome: '))
            
    elif opcao == 4:
        nome = input('✨ Digite o nome a ser removido: ')
        if nome in nomes:
            nomes.remove(nome)
        else:
            print('❌ Nome não encontrado.')
            
    elif opcao == 5:
        print('\n✨ Saindo do programa... ✨')
        break
    
    else:        
        print('❌ Opção inválida. Tente novamente.')
        
        
    
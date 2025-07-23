# Crie um dicionário de contatos com nome e telefone:
# 1. Adicionar contato
# 2. Buscar um contato
# 3. Atualizar um contato existente
# 4. Remover um contato

#MELHORIAS: tratamento de erros e validação de entradas de números de telefone.

contatos = {}

while True:
    print(f'\n############ MENU ############')
    print(f'''
        1. Adicionar contato
        2. Buscar um contato
        3. Atualizar um contato existente
        4. Remover um contato
        5. Sair
          ''')
    
    opcao = int(input('✨ Digite a sua opção: '))
    
    if opcao == 1:
        nome = input('✨ Digite o nome do contato: ')
        telefone = input('✨ Digite o telefone do contato: ')
        
        contatos[nome] = telefone
        print(f'✅ Contato {nome} adicionado com sucesso!')
        
    elif opcao == 2:
        nome = input('✨ Digite o nome do contato a ser buscado: ')
        
        if nome in contatos:
            print(f'📞 Contato encontrado: {nome} - {contatos[nome]}')
        else:
            print('❌ Contato não encontrado.')
            
    elif opcao == 3:
        nome = input('✨ Digite o nome do contato a ser atualizado: ')
        
        if nome in contatos:
            contatos[nome] = input('✨ Digite o novo telefone: ')
            print(f'✅ Contato {nome} atualizado com sucesso!')
        else:
            print('❌ Contato não encontrado.')
            
    elif opcao == 4:
        nome = input('✨ Digite o nome do contato a ser removido: ')
        
        if nome in contatos:
            del contatos[nome]
            print(f'✅ Contato {nome} removido com sucesso!')
        else:
            print('❌ Contato não encontrado.')
            
    elif opcao == 5:
        print('\n✨ Saindo do programa... ✨')
        break
    
    else:
        print('❌ Opção inválida. Tente novamente.')
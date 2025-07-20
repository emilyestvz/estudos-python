# Solicite a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos **e** se tem carteira de motorista (pergunte com `input` se `sim` ou `não`).

idade = int(input(f'\nDigite a sua idade: '))
idade_verificada = 18 <= idade <= 30

print(f'Verficação de idade: {idade_verificada}')

cnh = input(f'\nVocê tem carteira de motorista? (sim/não): ').strip().lower()




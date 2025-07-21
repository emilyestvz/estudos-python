#  Peça a idade e informe se a pessoa é criança (até 12), adolescente (13–17), adulto (18–59) ou idoso (60+).

nome = input(f'\nDigite o nome da pessoa: ')
print(f'Olá, {nome}! ✨')

idade = int(input(f'\nDigite a sua idade: '))

if idade >= 60:
    print(f'{nome} é um idoso 👴👵')
elif idade >= 18:
    print(f'{nome} é um adulto 👨‍🦳👩‍🦳')
elif idade >= 13:
    print(f'{nome} é um adolescente 👦👧')
else:
    print(f'{nome} é uma criança 👶👧👦')

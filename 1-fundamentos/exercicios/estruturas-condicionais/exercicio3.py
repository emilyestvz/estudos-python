#  Peça a idade e informe se a pessoa é criança (até 12), adolescente (13–17), adulto (18–59) ou idoso (60+).

nome = input(f'\nDigite o nome da pessoa: ')
print(f'Olá, {nome}! ✨')

idade = int(input(f'\nDigite a sua idade: '))

if idade <= 12:
    print(f'{nome} é uma criança 👶')
elif 13 <= idade <= 17:
    print(f'{nome} é adolescente 🧑')
elif 18 <= idade <= 59:
    print(f'{nome} é adulta 👨')
else:
    print(f'{nome} é idosa 👴')
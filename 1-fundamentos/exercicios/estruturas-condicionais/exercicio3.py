# Solicite a nota de um aluno e diga se ele foi aprovado (nota ≥ 7), em recuperação (nota entre 5 e 6.9) ou reprovado (abaixo de 5).

nota = float(input(f'\nDigite a nota do aluno: '))

if nota >= 7:
    print(f'Aluno aprovado ✅')
elif 5 <= nota < 6.9:
    print(f'Aluno em recuperação ⚠️')
else:
    print(f'Aluno reprovado ❌')
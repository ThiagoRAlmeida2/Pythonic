# Um programa que leia as duas notas do aluno e mostre a sua media
# e no final diga se ele esta aprovado ou nao
nome = input('Digite seu nome: ')
print('Seja bem vindo {}!' .format(nome))

n1 = float(input('Digite a 1ª nota do aluno: '))
n2 = float(input('Digite a 2ª nota do aluno: '))
m = (n1+n2)/2

print('A sua media foi: {}' .format(m))
if m >= 7:
    print('Você foi aprovado, parabens {}!' .format(nome))
else:
    print('Você poderá fazer a recuperação!')

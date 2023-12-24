from _ast import Div

nome = str(input('Digite o seu nome: '))
idade = int(input('Digigite sua idade: '))
# usar o {} para chamar o comando, nesse caso (nome e idade)
print('Bem vindo {}!! Você tem {} anos de idade. Correto??'.format(nome, idade))

print('Vamos usar a calculadora por um instante??')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
Soma = n1 + n2
Mult = n1 * n2
Divi = n1 / n2
Sub = n1 - n2
# Posso usar o () para chamar o format de (soma, mult, Divi, Sub)
print('A soma entre {} e {} é:{} ' .format(n1, n2, Soma))
print('A multiplicacao entre {} e {} é:{} ' .format(n1, n2, Mult))
print('A divisao entre {} e {} é:{} ' .format(n1, n2, Div))
print('A subtração entre {} e {} é:{} ' .format(n1, n2, Sub))

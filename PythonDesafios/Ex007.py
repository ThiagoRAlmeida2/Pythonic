nome = input('Digite o seu nome')
print('Prazer em te conhecer {}!'.format(nome))
# {:=^} {:>} {:<} para fazer alinhamentos

print('Vamos usar a calculadora por um instante??')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
p = n1 ** n2
r = n1 % n2

# Posso usar o () para chamar o format de (soma, mult, Divi, Sub)
print('A soma entre {} e {} é:{} '.format(n1, n2, s))
print('A multiplicacao entre {} e {} é:{} '.format(n1, n2, m))
print('A divisao entre {} e {} é:{:.3f} '.format(n1, n2, d))
print('A subtração entre {} e {} é:{} '.format(n1, n2, sub))
print('A divisao inteira entre {} e {} é: {}'.format(n1, n2, di))
print('A potencia entre {} e {} é:{} '.format(n1, n2, p))
print('O resto da divisão entre {} e {} é: {}'.format(n1, n2, r))

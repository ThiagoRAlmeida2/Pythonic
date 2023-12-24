n = input('Digite uma letra: ')
print('O tipo primitivo é: ', type(n))

print('Verificar propriedades da entrada: ')
print('É um número? ', n.isnumeric())  # Para verificar se é um numero
print('É uma letra? ', n.isalpha())  # Para verificar se é um alfabeto
print('É um número e uma letra? ', n.isalnum())  # Para verificar se tem um numero e uma letra
print('Tem apenas letras maiusculas? ', n.isupper())  # Para verifcar se tem apenas letras maiusculas
print('Tem apenas letras minusculas? ', n.islower())  # Para verificar se tem apenas letras minusculas
print('Só tem espaços? ', n.isspace())  # Para verificar se tem apenas espaços
print('Está capitalizado? ', n.istitle())  # Para dizer que tem letra Minusculas e Maiusculas

# Crie um programa que peça um valor em metros
# E o seu resultado tenha que ser em centimetro e em milimetros
metros = float(input('Digite a quantidades de metros desejada: '))
cm = metros * 100
mm = metros * 1000
print('A converção de metros para centimetros é {}cm ' .format(cm))
print('A converção de metros para milimetros é {}mm ' .format(mm))
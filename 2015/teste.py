numero = int(input('Digite um numero a ser calculado: '))
print('''Qual dessas operacoes dece ser feita:
[1] Adição
[2] Subtraçao
[3] Multiplicação
[4] Divisão''')
operacao = str(input('Escolha a operaçao: '))
for c in range (1, 11, 1):
    if operacao == 1:
        adi = c + numero
        print('{} + {} = {}'.format(c, numero, adi))
    if operacao == 2:
        sub = c - numero
        print('{} - {} = {}'.format(c, numero, sub))
    if operacao == 3:
       mult= c * numero
       print('{} x {} = {}'.format(c, numero, mult))
    if operacao == 4:
        div = c / numero
        print('{} ÷ {} = {:.2f}'.format(c, numero, div))
print('A tabuada é essa!!!') 
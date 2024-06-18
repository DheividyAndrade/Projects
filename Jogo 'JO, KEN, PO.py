# jogo 'JO, KEN, POO!'

from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''
[ 0 ] Pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # COMPUTADOR jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE! ')
    elif jogador == 2:
        print('COMPUTADOR VENCE! ')
    else:
        print('JOGADA INVALIDA!')
if computador == 1: # COMPUTADOR jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE! ')
    elif jogador == 1:
        print('EMPATE! ')
    elif jogador == 2:
        print('JOGADOR VENCE! ')
    else:
        print('JOGADA INVALIDA!')
if computador == 2: # COMPUTADOR jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE! ')
    elif jogador == 1:
        print('COMPUTADOR VENCE! ')
    elif jogador == 2:
        print('EMPATE! ')
    else:
        print('JOGADA INVALIDA!')
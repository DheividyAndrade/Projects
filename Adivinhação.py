# Faça um programa onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar entre um numero entre 0 e 10')
print('Sera que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... Tente novamente. ')
        elif jogador > computador:
            print('MENOS! Tente novamente. ')
print('Acertou com {} palpites. PARABÉNS! '.format(palpites))
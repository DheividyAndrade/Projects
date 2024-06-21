# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ  VENCEU!')
            v += 1
        else:
            print('VOÇÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU! ')
            v += 1
        else:
            print('VOCÊ PERDEU! ')
            break
    print('Vamos jogar NOVAMENTE...')
print(f'GAME OVER! Você venceu {v} vezes')
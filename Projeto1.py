# Crie um programa que leia dois valores e mostre um menu na tela:

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa ''')
    opçao = int(input('>>>> Qual a sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))
    elif opçao == 2:
        soma2 = n1 * n2
        print('{} x {} é igual a {}'.format(n1, n2, soma2))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o MAIOR É {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe outros numeros:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção invalida! tente novamente. ')
    print('=-=' * 10)
    sleep(2)
print('fim do programa! volte sempre. ')

from random import randint
from time import sleep
import os
import sys
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\33[35m',
    'verdeAgua': '\033[36m',
    'cinza': '\033[37m',
    

    'fundo preto ': '\033[40m',
    'fundo vermelho ': '\033[41m',
    'fundo verde ': '\033[42m',
    'fundo amarelo ': '\033[43m',
    'fundo azul': '\033[44m',
    'fundo magenta ': '\033[45m',
    'fundo ciano ': '\033[46m',
    'fundo branco': '\033[47m',

}

print('\n' + '-=' * 15 + ' GAME: Pedra Papel e Tesoura ' + '-=' * 15 + '\n')

nome = str(input('{}Digite o nome do jogador:{} ' .format(
    cores['azul'], cores['limpa']))).strip().upper()

resp = str('s').strip().lower()

while resp == str('s'):
    print('{}Suas opçõe: [0] PEDRA , [1] PAPEL , [2] TESOURA{}'.format(
        cores['roxo'], cores['limpa']))

    jogador = int(input('{}Qual a sua jogada ? '.format(cores['amarelo'])))
    if jogador > 2:
        print('\nJogada invalida')

        print('-=' * 15)
        print('Deseja continuar !!!')
        resp = str(input(
                    '{}Deseja jogar novamente? [S/N]: '.format(cores['limpa']))).strip().lower()

        if str('s') != resp != str('n'):

            while str('s') != resp != str('n'):
                print('Digito inválido ,tente novamente !')
                resp = str(input(
                    '{}Deseja jogar novamente? [S/N]: '.format(cores['limpa']))).strip().lower()

        print('-=' * 15 + '\n' * 40)

        # os.system("clear") funciona somente no Linux

    else:
        itens = ('PEDRA', 'PAPEL', 'TESOURA')
        comp = randint(0, 2)

        print('JO')
        sleep(0.7)
        print('KEN')
        sleep(0.7)
        print('PO!!!')
        sleep(0.7)

        print('-=' * 10)
        print('COMPUTADOR Jogou {}'.format(itens[comp]))
        print('(JOGADOR){} Jogou {}'.format(nome, itens[jogador]))
        print('-=' * 10)

        if comp == jogador:
            print('Empate')
        elif (comp == 0 and jogador == 1) \
                or (comp == 1 and jogador == 2) \
                or (comp == 2 and jogador == 0):

            print('(JOGADOR){} Venceu !!!'.format(nome))
        else:
            print('COMPUTADOR Venceu !!!')

        print('-=' * 15)
        print('Deseja continuar !!!')

        resp = str(input(
            '{}Deseja jogar novamente? [S/N]: '.format(cores['limpa']))).strip().lower()
        if str('s') != resp != str('n'):

            while str('s') != resp != str('n'):
                print('Digito inválido ,tente novamente !')
                resp = str(input(
                    '{}Deseja jogar novamente? [S/N]: '.format(cores['limpa']))).strip().lower()
        print('-=' * 15 + '\n' * 40)
        # os.system("clear") funciona somente no Linux

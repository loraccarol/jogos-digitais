# LABORATÓRIO 1
# Carolina Carvalho dos Santos TIA: 32129645

import random


def ex1():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    n3 = int(input('Número 3: '))

    maior = n1

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n1 == n2 & n2 == n2:
        print('Todos os números são iguais')
    else:
        print(maior, 'É o maior número')


def ex2():
    lista_valores = []

    def valor_pagamento(v, dias):
        multa = v * 0.03
        juros_por_dia = dias * 0.1

        if dias != 0:
            v += multa + juros_por_dia

        print(f'Valor a ser pago: R${v}')
        lista_valores.append(v)

    valor = 1
    while valor != 0:
        valor = float(input('Qual o valor da prestação? '))

        if valor == 0:
            print(f'=======================\n'
                  f'Relatório do dia: \n'
                  f'Quantidade de prestações: {len(lista_valores)}\n'
                  f'Valor total pago de prestações: {sum(lista_valores)}')
            break

        dias_atraso = int(input('Quantos dias de atraso? '))

        valor_pagamento(valor, dias_atraso)


def ex3():
    def baralho(carta, naipe):
        if carta == 1:
            carta = "Ás"
        elif carta == 11:
            carta = "J"
        elif carta == 12:
            carta = "Q"
        elif carta == 13:
            carta = "K"

        if naipe == 1:
            naipe = "PAUS"
        elif naipe == 2:
            naipe = "ESPADAS"
        elif naipe == 3:
            naipe = "OUROS"
        elif naipe == 4:
            naipe = "COPAS"
        print(f'{carta} de {naipe}')

    for i in range(5):
        lista_cartas = random.sample(range(1, 14), 5)
        lista_naipes = random.randrange(1, 5)
        baralho(lista_cartas[i], lista_naipes)


def main():
    opc = 0
    while opc != 4:
        print('===========================\n'
              '1- Retornar maior número\n'
              '2- Relatório de prestações\n'
              '3- Mostrar cinco cartas do baralho\n'
              '4- SAIR')
        opc = int(input('Escolha um exercício do laboratório 1: '))
        if opc == 1:
            ex1()
        elif opc == 2:
            ex2()
        elif opc == 3:
            ex3()
        else:
            break


main()

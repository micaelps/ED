from ContaCorrente import ContaCorrente
from Services import sacar,depositar,saldo



arrayContas = []

for i in range(2):
    numero = int(input('digite o numero: '))
    sal = float(input('digite o saldo inicial: '))
    nome_titular = input('digite o nome do titular: ')
    print('\n')
    arrayContas.append(ContaCorrente(numero,sal,nome_titular))



while True:
    print('''

1) DEPOSITAR
2) SACAR
3) SALDO
4) SAIR

    ''')

    menu = int(input('escolha >'))


    if menu == 1:
        numero = int(input('digite o numero da conta: '))
        valor = float(input('digite o valor a ser depositado: '))
        depositar(numero,valor, arrayContas)


    elif menu ==2:
        numero = int(input('digite o numero da conta: '))
        valor = float(input('digite o valor a ser depositado: '))
        sacar(numero,valor,arrayContas)


    elif menu==3:
        numero = int(input('digite o numero da conta: '))
        retorno = saldo(numero,arrayContas)
        print(f'o saldo atual é: {retorno}')
        input







from ContaCorrente import ContaCorrente


def depositar(numero,valor,arrayConta: ContaCorrente):
    for i in arrayConta:
        if i.numero == numero:
            i.depositar(valor)

def sacar(numero, valor, arrayConta:ContaCorrente):
     for i in arrayConta:
        if i.numero == numero:
            i.sacar(valor)

def saldo(numero, arrayConta: ContaCorrente):
    for i in arrayConta:
        if i.numero == numero:
            return i.saldo



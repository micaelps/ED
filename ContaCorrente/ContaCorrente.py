class ContaCorrente:
    def __init__(self, numero, saldo:float, nome_titular):
        self.numero = numero
        self.saldo = saldo
        self.nome_titular = nome_titular

    def depositar(self, valor):
        self.saldo+=valor
    
    def sacar(self, valor):
        if valor<self.saldo:
            self.saldo-=valor
            return True
        return False


    
        
    
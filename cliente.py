class Cliente:
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depositar de R${valor:.2f} realizar. Novo saldo: R${self.saldo:.2f}")
        else:
            print("O valor de deposito deve ser positivo.")

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print("Retirada de R$ {valor:.2f} realizadio. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para retirada.")

    def exibir_saldo(self):
        print(f"Cliente:{self.nome} | Saldo atual: R${self.salçdo:.2f}")
        


        # Exemplo de uso
        cliente1 = Cliente("João", 100.0)
        cliente1.exibir_saldo()
        cliente1.depositar(50.0)
        cliente1.retirar(30.0)
        cliente1.retirar(150.0)
        cliente1.exibir_saldo()

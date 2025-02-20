

class Cliente:
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("O valor de depósito deve ser positivo.")

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Retirada de R${valor:.2f} realizada. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para retirada.")

    def exibir_saldo(self):
        print(f"Cliente: {self.nome} | Saldo atual: R${self.saldo:.2f}")

    def exibir_nome(self):
        print(f"Cliente: {self.nome}")

# Exemplo de uso
cliente1 = Cliente("Luiz Paulo", 100.0)
cliente1.exibir_nome()
cliente1.exibir_saldo()
cliente1.depositar(500)
cliente1.retirar(30)
cliente1.exibir_saldo()

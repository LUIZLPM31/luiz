class Pessoa:
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf

    def getNome(self):
        print("Nome:" + self.nome)

class PessoaJuridica:
    def __init__(self, pessoa, cnpj):
        self.pessoa = pessoa
        self.cnpj = cnpj

    def getCNPJ(self):
        print(f"Nome: {self.pessoa.nome}, CNPJ: {self.cnpj}")

# Instantiate objects outside the class definitions
Pessoa1 = Pessoa('Luiz', 'rua 3, numero 1', 123456)
Pessoa1.getNome()
PessoaPJ1 = PessoaJuridica(Pessoa1, 12345678)
PessoaPJ1.getCNPJ()
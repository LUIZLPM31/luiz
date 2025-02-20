import streamlit as st

class Escola:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def exibir_informacoes(self):
       st.text(f"Escola: {self.nome}, Endereço: {self.endereco}")

class Aluno:
    def __init__(self, nome, matricula, nascimento):
        self.nome = nome
        self.matricula = matricula
        self.nascimento = nascimento

    def exibir_informacoes(self):
        st.text(f"Aluno: {self.nome}, Matrícula: {self.matricula}, Nascimento: {self.nascimento}")

class Professor:
    def __init__(self, nome, disciplina, salario):
        self.nome = nome
        self.disciplina = disciplina
        self.salario = salario

    def exibir_informacoes(self):
        st.text(f"Professor: {self.nome}, Disciplina: {self.disciplina}, Salário: {self.salario}")

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_informacoes(self):
        st.text(f"Curso: {self.nome}, Código: {self.codigo}")

# Exemplo de uso
escola1 = Escola("Escola Primária", "Rua das Flores, 123")
escola1.exibir_informacoes()

aluno1 = Aluno("Luiz Paulo", "12345", "31/03/2000")
aluno1.exibir_informacoes()

professor1 = Professor("Marcos", "Informatica", 3000.0)
professor1.exibir_informacoes()

curso1 = Curso("TI", "MAT101")
curso1.exibir_informacoes()

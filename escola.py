
import streamlit as st
from datetime import datetime

class Escola:
    def __init__(self, nome, endereco, telefone, diretor, nivel_ensino):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone  
        self.diretor = diretor  
        self.nivel_ensino = nivel_ensino  
        self.alunos = []  
        self.cursos = []  

    def exibir_informacoes(self):
        st.title("Informações da Escola")
        st.markdown(f"""
        - **Nome:** {self.nome}
        - **Endereço:** {self.endereco}
        - **Telefone:** {self.telefone}
        - **Diretor:** {self.diretor}
        - **Nível de Ensino:** {self.nivel_ensino}
        """)
        st.selectbox("tipo",["escola particular","escola publica"])

class Aluno:
    def __init__(self, nome, matricula, nascimento, responsavel, turma):
        self.nome = nome
        self.matricula = matricula
        self.nascimento = datetime.strptime(nascimento, "%d/%m/%Y") 
        self.responsavel = responsavel  
        self.turma = turma  
        self.notas = {} 

    def exibir_informacoes(self):
        st.title("Dados do Aluno")
        st.markdown(f"""
        - **Nome:** {self.nome}
        - **Matrícula:** {self.matricula}
        - **Nascimento:** {self.nascimento.strftime('%d/%m/%Y')}
        - **Responsável:** {self.responsavel}
        - **Turma:** {self.turma}
        """)

class Professor:
    def __init__(self, nome, disciplina, salario, formacao, carga_horaria):
        self.nome = nome
        self.disciplina = disciplina
        self.salario = salario
        self.formacao = formacao  
        self.carga_horaria = carga_horaria  
        self.turmas = []  

    def exibir_informacoes(self):
        st.title("Dados do Professor")
        st.markdown(f"""
        - **Nome:** {self.nome}
        - **Disciplina:** {self.disciplina}
        - **Formação:** {self.formacao}
        - **Carga Horária:** {self.carga_horaria}h
        - **Salário:** R$ {self.salario:,.2f}
        """)

class Curso:
    def __init__(self, nome, codigo, carga_horaria_total, coordenador):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria_total = carga_horaria_total  
        self.coordenador = coordenador 
        self.disciplinas = []  

    def exibir_informacoes(self):
        st.title("Informações do Curso")
        st.markdown(f"""
        - **Nome:** {self.nome}
        - **Código:** {self.codigo}
        - **Carga Horária Total:** {self.carga_horaria_total}h
        - **Coordenador:** {self.coordenador.nome}
        """)
        tipo = st.selectbox("tipo",["curso presencial","curso EAD"])
# Exemplo de uso aprimorado
escola = Escola(
    nome="Escola Técnica QI",
    endereco="Av. Juca Batista, 111",
    telefone="(51) 98765-4321",
    diretor="Maria Silva",
    nivel_ensino="Ensino Médio Técnico"
)

professor1 = Professor(
    nome="Carlos Andrade",
    disciplina="Programação",
    salario=4500.00,
    formacao="Mestrado em Ciência da Computação",
    carga_horaria=40
)

curso_ti = Curso(
    nome="Técnico em Informática",
    codigo="TECINF2025",
    carga_horaria_total=1200,
    coordenador=professor1
)

aluno = Aluno(
    nome="Luiz Paulo",
    matricula="2023001",
    nascimento="15/07/2005",
    responsavel="José ",
    turma="INFO101"
)

# Exibindo as informações
escola.exibir_informacoes()
st.divider()
professor1.exibir_informacoes()
st.divider()
curso_ti.exibir_informacoes()
st.divider()
aluno.exibir_informacoes()

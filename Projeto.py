#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install faker')


# In[26]:


get_ipython().system('pip install faker mysql-connector-python')

from dotenv import load_dotenv
import os
import random
from faker import Faker
import mysql.connector
from mysql.connector import errorcode

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='file.env')

# Configuração do banco de dados usando variáveis de ambiente
config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'raise_on_warnings': True
}

# Conectar ao banco de dados MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está errado com seu nome de usuário ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(err)
else:
    print("Conectado ao banco de dados")



# Criar as tabelas
def create_tables(cursor):
    tables = {}

    tables['Departamento'] = (
        "CREATE TABLE IF NOT EXISTS Departamento ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  Nome VARCHAR(100),"
        "  Chefe_Departamento INT"
        ")"
    )

    tables['Professor'] = (
        "CREATE TABLE IF NOT EXISTS Professor ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  Nome VARCHAR(100),"
        "  ID_Departamento INT,"
        "  FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID)"
        ")"
    )

    tables['Curso'] = (
        "CREATE TABLE IF NOT EXISTS Curso ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  Nome VARCHAR(100),"
        "  ID_Departamento INT,"
        "  FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID)"
        ")"
    )

    tables['Aluno'] = (
        "CREATE TABLE IF NOT EXISTS Aluno ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  Nome VARCHAR(100),"
        "  Matricula VARCHAR(20),"
        "  DataNascimento DATE,"
        "  ID_Curso INT,"
        "  FOREIGN KEY (ID_Curso) REFERENCES Curso(ID)"
        ")"
    )

    tables['Disciplina'] = (
        "CREATE TABLE IF NOT EXISTS Disciplina ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  Nome VARCHAR(100),"
        "  ID_Curso INT,"
        "  FOREIGN KEY (ID_Curso) REFERENCES Curso(ID)"
        ")"
    )

    tables['MatrizCurricular'] = (
        "CREATE TABLE IF NOT EXISTS MatrizCurricular ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  ID_Curso INT,"
        "  ID_Disciplina INT,"
        "  Semestre INT,"
        "  FOREIGN KEY (ID_Curso) REFERENCES Curso(ID),"
        "  FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID)"
        ")"
    )

    tables['HistoricoEscolar'] = (
        "CREATE TABLE IF NOT EXISTS HistoricoEscolar ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  ID_Aluno INT,"
        "  ID_Disciplina INT,"
        "  Semestre INT,"
        "  Ano INT,"
        "  NotaFinal FLOAT,"
        "  FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID),"
        "  FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID)"
        ")"
    )

    tables['DisciplinasMinistradas'] = (
        "CREATE TABLE IF NOT EXISTS DisciplinasMinistradas ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  ID_Professor INT,"
        "  ID_Disciplina INT,"
        "  Semestre INT,"
        "  Ano INT,"
        "  FOREIGN KEY (ID_Professor) REFERENCES Professor(ID),"
        "  FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID)"
        ")"
    )

    tables['TCC'] = (
        "CREATE TABLE IF NOT EXISTS TCC ("
        "  ID INT PRIMARY KEY AUTO_INCREMENT,"
        "  ID_Aluno INT,"
        "  ID_Professor INT,"
        "  Titulo VARCHAR(200),"
        "  Semestre INT,"
        "  Ano INT,"
        "  FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID),"
        "  FOREIGN KEY (ID_Professor) REFERENCES Professor(ID)"
        ")"
    )

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

# Limpar tabelas
def clear_tables(cursor):
    tables = [
        'HistoricoEscolar',
        'DisciplinasMinistradas',
        'TCC',
        'MatrizCurricular',
        'Aluno',
        'Disciplina',
        'Curso',
        'Professor',
        'Departamento'
    ]
    for table in tables:
        try:
            cursor.execute(f"DELETE FROM {table}")
            cursor.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1")
        except mysql.connector.Error as err:
            print(f"Erro ao limpar tabela {table}: {err}")

# Gerar dados aleatórios
fake = Faker()

def generate_departments(cursor, num):
    departments = [(fake.company(),) for _ in range(num)]
    cursor.executemany("INSERT INTO Departamento (Nome) VALUES (%s)", departments)
    cursor.execute("SELECT ID FROM Departamento")
    department_ids = [row[0] for row in cursor.fetchall()]

    return department_ids

def generate_professors(cursor, num, department_ids):
    professors = [(fake.name(), random.choice(department_ids)) for _ in range(num)]
    cursor.executemany("INSERT INTO Professor (Nome, ID_Departamento) VALUES (%s, %s)", professors)
    cursor.execute("SELECT ID FROM Professor")
    return [row[0] for row in cursor.fetchall()]

def assign_chefe_departamento(cursor, department_ids, professor_ids):
    for dept_id in department_ids:
        chefe_id = random.choice(professor_ids)
        cursor.execute("UPDATE Departamento SET Chefe_Departamento = %s WHERE ID = %s", (chefe_id, dept_id))

def generate_courses(cursor, num, department_ids):
    courses = [(fake.job(), random.choice(department_ids)) for _ in range(num)]
    cursor.executemany("INSERT INTO Curso (Nome, ID_Departamento) VALUES (%s, %s)", courses)
    cursor.execute("SELECT ID FROM Curso")
    return [row[0] for row in cursor.fetchall()]

def generate_students(cursor, num, course_ids):
    students = [(fake.name(), fake.bothify(text='??######'), fake.date_of_birth(), random.choice(course_ids)) for _ in range(num)]
    cursor.executemany("INSERT INTO Aluno (Nome, Matricula, DataNascimento, ID_Curso) VALUES (%s, %s, %s, %s)", students)

def generate_disciplines(cursor, num, course_ids):
    disciplines = [(fake.catch_phrase(), random.choice(course_ids)) for _ in range(num)]
    cursor.executemany("INSERT INTO Disciplina (Nome, ID_Curso) VALUES (%s, %s)", disciplines)

def generate_matriz_curricular(cursor, num, course_ids):
    matriz = [(random.choice(course_ids), random.randint(1, num), random.randint(1, 8)) for _ in range(num)]
    cursor.executemany("INSERT INTO MatrizCurricular (ID_Curso, ID_Disciplina, Semestre) VALUES (%s, %s, %s)", matriz)

def generate_historico_escolar(cursor, num):
    historico = [(random.randint(1, num), random.randint(1, num), random.randint(1, 8), fake.year(), random.uniform(0, 10)) for _ in range(num)]
    cursor.executemany("INSERT INTO HistoricoEscolar (ID_Aluno, ID_Disciplina, Semestre, Ano, NotaFinal) VALUES (%s, %s, %s, %s, %s)", historico)

def generate_disciplinas_ministradas(cursor, num):
    disciplinas = [(random.randint(1, num), random.randint(1, num), random.randint(1, 8), fake.year()) for _ in range(num)]
    cursor.executemany("INSERT INTO DisciplinasMinistradas (ID_Professor, ID_Disciplina, Semestre, Ano) VALUES (%s, %s, %s, %s)", disciplinas)

def generate_tcc(cursor, num):
    tcc = [(random.randint(1, num), random.randint(1, num), fake.sentence(nb_words=6), random.randint(1, 8), fake.year()) for _ in range(num)]
    cursor.executemany("INSERT INTO TCC (ID_Aluno, ID_Professor, Titulo, Semestre, Ano) VALUES (%s, %s, %s, %s, %s)", tcc)

# Inserir dados em blocos menores
def insert_data_in_batches(generator_function, cursor, cnx, num, batch_size=20, *args):
    for i in range(0, num, batch_size):
        print(f"Inserting batch {i} to {i + batch_size}")
        generator_function(cursor, min(batch_size, num - i), *args)
        cnx.commit()

# Criar e popular o banco de dados
def create_and_populate_database():
    create_tables(cursor)
    
    department_ids = generate_departments(cursor, 10)
    cnx.commit()

    professor_ids = generate_professors(cursor, 50, department_ids)
    cnx.commit()
    
    assign_chefe_departamento(cursor, department_ids, professor_ids)
    cnx.commit()

    course_ids = generate_courses(cursor, 20, department_ids)
    cnx.commit()

    insert_data_in_batches(generate_students, cursor, cnx, 200, 20, course_ids)
    insert_data_in_batches(generate_disciplines, cursor, cnx, 100, 20, course_ids)
    insert_data_in_batches(generate_matriz_curricular, cursor, cnx, 100, 20, course_ids)
    insert_data_in_batches(generate_historico_escolar, cursor, cnx, 500, 20)
    insert_data_in_batches(generate_disciplinas_ministradas, cursor, cnx, 200, 20)
    insert_data_in_batches(generate_tcc, cursor, cnx, 50, 20)

create_and_populate_database()

# Fechar a conexão
cursor.close()
cnx.close()


# In[20]:


pip install python-dotenv


# In[ ]:





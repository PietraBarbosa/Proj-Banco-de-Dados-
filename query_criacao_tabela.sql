CREATE TABLE Departamento (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Chefe_Departamento INT,
    FOREIGN KEY (Chefe_Departamento) REFERENCES Professor(ID)
);

CREATE TABLE Professor (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    ID_Departamento INT,
    FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID)
);

CREATE TABLE Curso (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    ID_Departamento INT,
    FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID)
);

CREATE TABLE Aluno (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Matricula VARCHAR(20),
    DataNascimento DATE,
    ID_Curso INT,
    FOREIGN KEY (ID_Curso) REFERENCES Curso(ID)
);

CREATE TABLE Disciplina (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    ID_Curso INT,
    FOREIGN KEY (ID_Curso) REFERENCES Curso(ID)
);

CREATE TABLE MatrizCurricular (
    ID INT PRIMARY KEY,
    ID_Curso INT,
    ID_Disciplina INT,
    Semestre INT,
    FOREIGN KEY (ID_Curso) REFERENCES Curso(ID),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID)
);

CREATE TABLE HistoricoEscolar (
    ID INT PRIMARY KEY,
    ID_Aluno INT,
    ID_Disciplina INT,
    Semestre INT,
    Ano INT,
    NotaFinal FLOAT,
    FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID)
);

CREATE TABLE DisciplinasMinistradas (
    ID INT PRIMARY KEY,
    ID_Professor INT,
    ID_Disciplina INT,
    Semestre INT,
    Ano INT,
    FOREIGN KEY (ID_Professor) REFERENCES Professor(ID),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID)
);

CREATE TABLE TCC (
    ID INT PRIMARY KEY,
    ID_Aluno INT,
    ID_Professor INT,
    Titulo VARCHAR(200),
    Semestre INT,
    Ano INT,
    FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID),
    FOREIGN KEY (ID_Professor) REFERENCES Professor(ID)
);

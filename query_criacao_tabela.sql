CREATE TABLE IF NOT EXISTS Departamento ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           Nome VARCHAR(100), 
           Chefe_Departamento INT 
         ) ;
		

CREATE TABLE IF NOT EXISTS Professor ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           Nome VARCHAR(100), 
           ID_Departamento INT, 
           FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS Curso ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           Nome VARCHAR(100), 
           ID_Departamento INT, 
           FOREIGN KEY (ID_Departamento) REFERENCES Departamento(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS Aluno ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           Nome VARCHAR(100), 
           Matricula VARCHAR(20), 
           DataNascimento DATE, 
           ID_Curso INT, 
           FOREIGN KEY (ID_Curso) REFERENCES Curso(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS Disciplina ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           Nome VARCHAR(100), 
           ID_Curso INT, 
           FOREIGN KEY (ID_Curso) REFERENCES Curso(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS MatrizCurricular ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           ID_Curso INT, 
           ID_Disciplina INT, 
           Semestre INT, 
           FOREIGN KEY (ID_Curso) REFERENCES Curso(ID), 
           FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS HistoricoEscolar ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           ID_Aluno INT, 
           ID_Disciplina INT, 
           Semestre INT, 
           Ano INT, 
           NotaFinal FLOAT, 
           FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID), 
           FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS DisciplinasMinistradas ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           ID_Professor INT, 
           ID_Disciplina INT, 
           Semestre INT, 
           Ano INT, 
           FOREIGN KEY (ID_Professor) REFERENCES Professor(ID), 
           FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID) 
         ) ;
		
CREATE TABLE IF NOT EXISTS TCC ( 
           ID INT PRIMARY KEY AUTO_INCREMENT, 
           ID_Aluno INT, 
           ID_Professor INT, 
           Titulo VARCHAR(200), 
           Semestre INT, 
           Ano INT, 
           FOREIGN KEY (ID_Aluno) REFERENCES Aluno(ID), 
           FOREIGN KEY (ID_Professor) REFERENCES Professor(ID) 
         ) ;
# Proj-Banco-de-Dados-

## Integrantes do Grupo

- João Victor Castilho de Sá Freire - RA: 22.121.032-1
- Pietra Marques Barbosa - RA: 22.121.124-6

## Como Executar

## Diagrama Relacional

```mermaid
erDiagram
    ALUNO {
        int ID
        string Nome
        string Matricula
        date DataNascimento
        int ID_Curso
    }
    
    PROFESSOR {
        int ID
        string Nome
        int ID_Departamento
    }
    
    CURSO {
        int ID
        string Nome
        int ID_Departamento
    }
    
    DEPARTAMENTO {
        int ID
        string Nome
        int Chefe_Departamento
    }
    
    DISCIPLINA {
        int ID
        string Nome
        int ID_Curso
    }
    
    MATRIZCURRICULAR {
        int ID
        int ID_Curso
        int ID_Disciplina
        int Semestre
    }
    
    HISTORICOESCOLAR {
        int ID
        int ID_Aluno
        int ID_Disciplina
        int Semestre
        int Ano
        float NotaFinal
    }
    
    DISCIPLINASMINISTRADAS {
        int ID
        int ID_Professor
        int ID_Disciplina
        int Semestre
        int Ano
    }
    
    TCC {
        int ID
        int ID_Aluno
        int ID_Professor
        string Titulo
        int Semestre
        int Ano
    }

    ALUNO ||--o{ CURSO: "matricula em"
    PROFESSOR ||--o{ DEPARTAMENTO: "pertence a"
    CURSO ||--o{ DEPARTAMENTO: "oferecido por"
    DISCIPLINA ||--o{ CURSO: "parte de"
    MATRIZCURRICULAR ||--o{ CURSO: "define"
    MATRIZCURRICULAR ||--o{ DISCIPLINA: "inclui"
    HISTORICOESCOLAR ||--o{ ALUNO: "registro de"
    HISTORICOESCOLAR ||--o{ DISCIPLINA: "registro de"
    DISCIPLINASMINISTRADAS ||--o{ PROFESSOR: "leciona"
    DISCIPLINASMINISTRADAS ||--o{ DISCIPLINA: "ministrada"
    TCC ||--o{ ALUNO: "realizado por"
    TCC ||--o{ PROFESSOR: "orientado por"
    DEPARTAMENTO ||--o{ PROFESSOR: "chefe de"

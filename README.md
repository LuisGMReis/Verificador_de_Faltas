# Gerenciador de Disciplinas com Controle de Faltas

Este projeto é uma aplicação em Python que utiliza programação orientada a objetos para gerenciar disciplinas e controlar a situação de faltas dos alunos. A aplicação permite calcular o total de aulas, o limite de faltas permitido e verificar se o aluno está dentro ou fora do limite de faltas.

## Funcionalidades Principais

### 1. **Classe `Disciplina`**
   - **Atributos**:
     - `nome`: Nome da disciplina.
     - `carga_horaria`: Carga horária total da disciplina em horas.
     - `faltas`: Número de faltas do aluno.
     - `total_aulas`: Total de aulas calculado com base na carga horária.
     - `limite_faltas`: Limite de faltas permitido (25% da carga horária).

   - **Métodos**:
     - `validar_dados`: Valida se a carga horária e as faltas são valores válidos.
     - `_calcular_total_aulas`: Calcula o total de aulas com base na carga horária.
     - `_calcular_limite_faltas`: Calcula o limite de faltas permitido.
     - `verificar_situacao`: Verifica a situação do aluno em relação às faltas.

### 2. **Classe `DisciplinaError`**
   - **Herança de `Exception`**: Classe personalizada para tratar erros específicos relacionados à disciplina, como carga horária inválida ou número de faltas negativo.

### 3. **Funções Auxiliares**
   - `ler_entrada_numerica`: Função para ler e validar entradas numéricas do usuário.
   - `main`: Função principal que coordena o fluxo do programa, incluindo a entrada de dados, criação da disciplina e exibição dos resultados.

## Estrutura do Código

### 1. **Classe `Disciplina`**
   - **Constantes**:
     - `DURACAO_AULA`: Duração de cada aula em minutos (50 minutos).
     - `LIMITE_FALTAS`: Limite de faltas permitido (25% da carga horária).

   - **Método Construtor (`__init__`)**:
     - Inicializa os atributos da disciplina e realiza validações dos dados de entrada.

   - **Métodos Privados**:
     - `_calcular_total_aulas`: Calcula o total de aulas com base na carga horária.
     - `_calcular_limite_faltas`: Calcula o limite de faltas permitido.

   - **Método Público**:
     - `verificar_situacao`: Retorna uma mensagem indicando a situação do aluno em relação às faltas.

### 2. **Função `ler_entrada_numerica`**
   - **Validação de Entrada**: Garante que o usuário insira um valor numérico válido.

### 3. **Função `main`**
   - **Fluxo do Programa**:
     - Solicita ao usuário o nome da disciplina, a carga horária e o número de faltas.
     - Cria uma instância da classe `Disciplina`.
     - Exibe o total de aulas e a situação do aluno em relação às faltas.

## Como Executar

1. **Instalação do Python**:
   - Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

2. **Execução do Programa**:
   - Salve o código em um arquivo com extensão `.py`, por exemplo, `gerenciador_disciplinas.py`.
   - Execute o arquivo usando o Python:
     ```bash
     python gerenciador_disciplinas.py
     ```

3. **Entrada de Dados**:
   - O programa solicitará o nome da disciplina, a carga horária e o número de faltas.
   - Insira os valores solicitados e o programa exibirá o total de aulas e a situação do aluno.

## Exemplo de Uso

### Entrada:

Nome da matéria: Matemática
Carga Horária da matéria matemática: 60
Quantidade de Faltas na matéria matemática: 10
Copy


### Saída:

A matéria de matemática tem 60 horas e há 72 aulas.
Você ainda pode faltar 5 aulas.
Copy


## Considerações Finais

Este projeto é uma solução simples e eficaz para gerenciar disciplinas e controlar a situação de faltas dos alunos. Ele pode ser expandido para incluir mais funcionalidades, como o cálculo de notas, geração de relatórios ou integração com um banco de dados para armazenar as informações das disciplinas.

Para qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato!

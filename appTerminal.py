# Criamos uma classe de erro personalizada que herda de Exception
# Isso nos permite ter erros específicos do nosso domínio (disciplina)
class DisciplinaError(Exception):
    """Classe personalizada para erros relacionados à disciplina"""
    pass

# Classe principal que representa uma disciplina
# Usando programação orientada a objetos para melhor organização do código
class Disciplina:
    # Constantes da classe - Valores que não mudam e são compartilhados por todas as instâncias
    # Isso facilita a manutenção - se precisar mudar, muda em um só lugar
    DURACAO_AULA = 50  # minutos
    LIMITE_FALTAS = 0.25  # 25% da carga horária

    # Método construtor (__init__)
    # É chamado automaticamente quando criamos uma nova instância da classe
    # self representa a própria instância que está sendo criada
    def __init__(self, nome: str, carga_horaria: int, faltas: int):
        # Inicialização dos atributos da instância
        self.nome = nome.lower()
        # Validação antes de criar o objeto
        self.validar_dados(carga_horaria, faltas)
        self.carga_horaria = carga_horaria
        self.faltas = faltas
        # Cálculos iniciais
        self.total_aulas = self._calcular_total_aulas()
        self.limite_faltas = self._calcular_limite_faltas()

    # Método estático (@staticmethod)
    # Não precisa de self pois não depende do estado do objeto
    # Pode ser chamado sem criar uma instância da classe
    @staticmethod
    def validar_dados(carga_horaria: int, faltas: int) -> None:
        """Valida os dados de entrada da disciplina"""
        if carga_horaria <= 0:
            raise DisciplinaError("A carga horária deve ser um valor positivo.")
        if faltas < 0:
            raise DisciplinaError("As faltas devem ser um valor não negativo.")

    # Métodos privados (começam com _)
    # São métodos auxiliares que só devem ser usados dentro da classe
    def _calcular_total_aulas(self) -> float:
        """Calcula o total de aulas baseado na carga horária"""
        return (self.carga_horaria * 60) / self.DURACAO_AULA

    def _calcular_limite_faltas(self) -> float:
        """Calcula o limite de faltas permitido"""
        return self.carga_horaria * self.LIMITE_FALTAS

    # Método público que verifica a situação do aluno
    # Retorna uma tupla com a mensagem e o número de faltas (positivo ou negativo)
    def verificar_situacao(self) -> tuple[str, float]:
        """Verifica a situação do aluno em relação às faltas"""
        if self.faltas < self.limite_faltas:
            faltas_restantes = self.limite_faltas - self.faltas
            return f"Você ainda pode faltar {faltas_restantes:.0f} aulas.", faltas_restantes
        elif self.faltas == self.limite_faltas:
            return "Você não pode mais faltar.", 0
        else:
            excesso_faltas = self.faltas - self.limite_faltas
            return f"Você ultrapassou o limite de {self.limite_faltas:.0f} faltas permitidas com {excesso_faltas:.0f} faltas a mais.", -excesso_faltas

# Função auxiliar para tratar entrada de dados
# Separada da classe pois não está diretamente relacionada com a disciplina
def ler_entrada_numerica(mensagem: str) -> int:
    """Função auxiliar para ler e validar entrada numérica"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número válido.")

# Função principal que coordena o fluxo do programa
def main():
    """Função principal do programa"""
    try:
        # Entrada de dados com tratamento de erro
        nome = input("Nome da matéria: ")
        carga_horaria = ler_entrada_numerica(f"Carga Horária da matéria {nome.lower()}: ")
        faltas = ler_entrada_numerica(f"Quantidade de Faltas na matéria {nome.lower()}: ")

        # Criação da disciplina - se houver erro na validação, será capturado pelo try/except
        disciplina = Disciplina(nome, carga_horaria, faltas)
        
        # Exibição dos resultados
        print(f"\nA matéria de {disciplina.nome} tem {disciplina.carga_horaria} horas "
                f"e há {disciplina.total_aulas:.0f} aulas.")
        
        mensagem, _ = disciplina.verificar_situacao()
        print(mensagem)

    except DisciplinaError as e:
        print(f"Erro: {str(e)}")

# Isso garante que o código só será executado se este arquivo for o principal
# Se o arquivo for importado como módulo em outro lugar, main() não será executado
if __name__ == "__main__":
    main()
# Entrada da variável matéria
materia = input("Nome da matéria: ")
materiaLower = materia.lower()

# Verificação de dados inseridos pelo usuário
while True:
    try:
        cargaH = int(input(f"Carga Horária da matéria {materiaLower}: "))
        
        if cargaH <= 0:
            print("A carga horária deve ser um valor positivo. Tente novamente.")
            continue
        
        faltas = int(input(f"Quantidade de Faltas na matéria {materiaLower}: "))
        if faltas < 0:
            print("As faltas devem ser um valor não negativo. Tente novamente.\n")  # \n para separar os erros anteriores
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido.")

# Função de cálculo
def operacao(cargaH):
    cargaHemM = cargaH * 60  # Carga horária em minutos
    qtdAulas = cargaHemM / 50  # Quantidade de aulas
    vcpDaMat = cargaH * 0.25  # Limiar de decisão (25% da matéria)
    return vcpDaMat, qtdAulas

# Chamada da função e captura dos valores retornados
vcp, qtdAulas = operacao(cargaH)

# Condições
if faltas < vcp:
    podeFaltar = vcp - faltas
    print(f"\nA matéria de {materiaLower} tem {cargaH} horas e há {qtdAulas:.0f} aulas.")
    print(f"Você ainda pode faltar {podeFaltar:.0f} aulas.")

elif faltas == vcp:
    print(f"\nA matéria de {materiaLower} tem {cargaH} horas e há {qtdAulas:.0f} aulas.")
    print("Você não pode mais faltar.")

else:  # faltas > vcp
    faltasAmais = faltas - vcp
    print(f"\nA matéria de {materiaLower} tem {cargaH} horas e há {qtdAulas:.0f} aulas.")
    print(f"Você ultrapassou o limite de {vcp:.0f} faltas permitidas com {faltasAmais:.0f} faltas a mais.")
